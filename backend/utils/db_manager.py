# -*- coding: utf-8 -*-
"""
db_manager.py

A database utility module for managing predictions history and contact messages 
using an SQLite database. It provides helpers to insert, query, and get aggregated analytics,
and seeds mock data on startup if tables are empty.

Author: AgriAI Developer Team
Date: June 24, 2026
"""

import os
import sqlite3
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "predictions.db")

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows
    return conn

def init_db():
    """Initializes the database schema and seeds sample data if tables are empty."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create predictions history table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            n REAL NOT NULL,
            p REAL NOT NULL,
            k REAL NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL,
            ph REAL NOT NULL,
            rainfall REAL NOT NULL,
            recommended_crop TEXT NOT NULL,
            confidence REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create contact messages table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Seed predictions if empty
    cursor.execute("SELECT COUNT(*) FROM predictions")
    if cursor.fetchone()[0] == 0:
        print("[INFO] Seeding default crop predictions history...")
        sample_preds = [
            (90, 42, 43, 20.8, 82.0, 6.5, 202.9, "Rice", 0.98, "2026-06-23 09:15:00"),
            (80, 50, 40, 25.0, 75.0, 6.8, 150.0, "Maize", 0.95, "2026-06-22 14:30:00"),
            (40, 60, 30, 18.0, 60.0, 7.2, 80.0, "Chickpea", 0.92, "2026-06-21 11:45:00")
        ]
        cursor.executemany("""
            INSERT INTO predictions (n, p, k, temperature, humidity, ph, rainfall, recommended_crop, confidence, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, sample_preds)
        
    # Seed messages if empty
    cursor.execute("SELECT COUNT(*) FROM contact_messages")
    if cursor.fetchone()[0] == 0:
        print("[INFO] Seeding default contact messages...")
        sample_msgs = [
            ("Rajesh Patil", "rajesh.patil@agrimail.com", "Drip Irrigation Advice", 
             "Requesting guidelines for setting up drip irrigation in red soil for my banana plantation.", 
             "2026-06-23 09:12:00"),
            ("Sukhwinder Singh", "sukhwinder.farm@punjabagro.co", "Soil pH Neutralizer", 
             "My soil test shows a high pH of 8.2. Which organic amendments do you suggest for neutralising before sowing wheat?", 
             "2026-06-22 16:30:00"),
            ("Ananya Rao", "ananya.rao@cottonfields.in", "Appreciation", 
             "The agricultural weather alert helped me delay my fertilizer application. Saved me ₹15,000 worth of chemicals!", 
             "2026-06-21 11:05:00")
        ]
        cursor.executemany("""
            INSERT INTO contact_messages (name, email, subject, message, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, sample_msgs)
        
    conn.commit()
    conn.close()
    print(f"[INFO] Database initialized and seeded at: {DB_PATH}")

def save_prediction(n, p, k, temp, humidity, ph, rainfall, crop, confidence):
    """Saves a single prediction record into the database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO predictions (n, p, k, temperature, humidity, ph, rainfall, recommended_crop, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (n, p, k, temp, humidity, ph, rainfall, crop, confidence))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save prediction to DB: {e}")
        return False

def get_history(limit=10):
    """Retrieves recent prediction records from the database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, n, p, k, temperature, humidity, ph, rainfall, recommended_crop, confidence, timestamp
            FROM predictions
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()
        
        history = []
        for r in rows:
            # Parse database timestamp
            try:
                dt = datetime.strptime(r["timestamp"], "%Y-%m-%d %H:%M:%S")
                date_str = dt.strftime("%d/%m/%Y %I:%M %p")
            except Exception:
                date_str = r["timestamp"]
                
            history.append({
                "id": r["id"],
                "n": r["n"],
                "p": r["p"],
                "k": r["k"],
                "temperature": r["temperature"],
                "humidity": r["humidity"],
                "ph": r["ph"],
                "rainfall": r["rainfall"],
                "crop": r["recommended_crop"],
                "confidence": f"{r['confidence'] * 100:.1f}%",
                "timestamp": date_str
            })
        return history
    except Exception as e:
        print(f"[ERROR] Failed to get prediction history: {e}")
        return []

def get_analytics():
    """Computes aggregate analytics of crop recommendation frequencies and total count."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Get total predictions in SQLite DB
        cursor.execute("SELECT COUNT(*) FROM predictions")
        total_predictions = cursor.fetchone()[0]
        
        # Get crop counts from SQLite DB
        cursor.execute("""
            SELECT recommended_crop, COUNT(*) as count 
            FROM predictions 
            GROUP BY recommended_crop
            ORDER BY count DESC
        """)
        rows = cursor.fetchall()
        conn.close()
        
        # Format crop counts dictionary
        # Start with standard baseline categories to match dashboard defaults
        counts = {
            "Rice": 420,
            "Maize": 310,
            "Chickpea": 180,
            "Cotton": 220,
            "Others": 150
        }
        
        # Add values from actual DB predictions to these categories
        for r in rows:
            crop_name = r["recommended_crop"].title()
            if crop_name in counts:
                counts[crop_name] += r["count"]
            else:
                counts["Others"] += r["count"]
                
        # Total mock+db count
        grand_total = 12840 + total_predictions
        
        return {
            "total_recommendations": grand_total,
            "crop_counts": counts,
            "db_only_predictions": total_predictions
        }
    except Exception as e:
        print(f"[ERROR] Failed to calculate database analytics: {e}")
        return {
            "total_recommendations": 12840,
            "crop_counts": {"Rice": 420, "Maize": 310, "Chickpea": 180, "Cotton": 220, "Others": 150},
            "db_only_predictions": 0
        }

def save_contact_message(name, email, subject, message):
    """Saves a contact form inquiry into the database."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contact_messages (name, email, subject, message)
            VALUES (?, ?, ?, ?)
        """, (name, email, subject, message))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save contact message: {e}")
        return False

def get_contact_messages(limit=20):
    """Retrieves list of contact queries sorted by date."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name, email, subject, message, timestamp
            FROM contact_messages
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))
        rows = cursor.fetchall()
        conn.close()
        
        messages = []
        for r in rows:
            # Parse datetime for nice printing
            try:
                dt = datetime.strptime(r["timestamp"], "%Y-%m-%d %H:%M:%S")
                date_str = dt.strftime("%d/%m/%Y %I:%M %p")
            except Exception:
                date_str = r["timestamp"]
                
            messages.append({
                "name": r["name"],
                "email": r["email"],
                "subject": r["subject"],
                "message": r["message"],
                "date": date_str
            })
        return messages
    except Exception as e:
        print(f"[ERROR] Failed to get contact messages: {e}")
        return []
