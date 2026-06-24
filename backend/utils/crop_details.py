# -*- coding: utf-8 -*-
"""
crop_details.py

Contains detailed metadata, scientific classifications, fertilizer recommendations,
expert tips, sustainable farming advice, and custom explanations for all 22 crops
in the Crop Recommendation Dataset.

Author: AgriAI Developer Team
Date: June 24, 2026
"""

CROP_DETAILS_DB = {
    "rice": {
        "name": "Rice (Oryza sativa)",
        "crop": "Rice",
        "icon": "🌾",
        "scientific": "Oryza sativa L.",
        "season": "Kharif (Monsoon)",
        "duration": "120 - 150 Days",
        "demand": "Very High",
        "price": "₹2,183 / Quintal",
        "fertilizer": "Nitrogen-rich fertilizer (Urea) in 3 split doses (basal, tillering, panicle initiation). Add Zinc Sulphate (25kg/ha) if leaves turn rusty brown.",
        "tips": "Maintain standing water of 2-5 cm during early vegetative phase. Drain fields 10-15 days before harvest for uniform ripening.",
        "explanation": "Recommended due to high humidity and high rainfall conditions. Rice thrives in clayey or loamy soils that can retain moisture well under wet seasonal dynamics.",
        "sustainable_tips": [
            "Adopt System of Rice Intensification (SRI) to reduce water requirements by 30-40% and increase yields.",
            "Utilize Alternate Wetting and Drying (AWD) irrigation to mitigate methane emission from flooded fields.",
            "Incorporate green manure crops like Sesbania (Daincha) before transplanting to enrich soil nitrogen naturally."
        ]
    },
    "maize": {
        "name": "Maize (Zea mays)",
        "crop": "Maize",
        "icon": "🌽",
        "scientific": "Zea mays L.",
        "season": "Kharif / Rabi",
        "duration": "95 - 115 Days",
        "demand": "High",
        "price": "₹2,090 / Quintal",
        "fertilizer": "Balanced NPK (120:60:40 kg/ha). Apply Di-Ammonium Phosphate (DAP) during sowing and top-dress with Urea at knee-high and tasseling stages.",
        "tips": "Ensure excellent soil drainage; maize is highly sensitive to waterlogging. Critical stages for irrigation are silking and grain filling.",
        "explanation": "Selected for moderate moisture, temperature, and well-drained loamy soil conditions. Maize requires high nutrient inputs and balanced aeration in root zones.",
        "sustainable_tips": [
            "Use crop residue mulching to retain soil moisture and reduce soil erosion in sloping terrains.",
            "Practice crop rotation with legumes like chickpea or soybean to break pest cycles and replenish soil nitrogen.",
            "Implement micro-dosing of fertilizer directly at the base of the plant to minimize run-off and maximize absorption."
        ]
    },
    "chickpea": {
        "name": "Chickpea (Cicer arietinum)",
        "crop": "Chickpea",
        "icon": "🧆",
        "scientific": "Cicer arietinum L.",
        "season": "Rabi (Winter)",
        "duration": "110 - 120 Days",
        "demand": "High",
        "price": "₹5,440 / Quintal",
        "fertilizer": "Low Nitrogen starter dose, High Phosphorus and Potassium. Treat seeds with Rhizobium culture to enhance natural nitrogen fixation.",
        "tips": "Avoid excessive irrigation to prevent vegetative run-away at the cost of pod formation. Nip top leaves at 30-40 days to promote branching.",
        "explanation": "Matches cold winter temperatures, low humidity, and moderate soil moisture. Chickpea is highly efficient in dryland farming with minimal rainfall.",
        "sustainable_tips": [
            "Apply bio-fertilizers like Phosphobacterins to solubilize fixed soil phosphorus for better root absorption.",
            "Practice conservation tillage to preserve stored soil moisture from previous monsoon rains.",
            "Adopt mixed cropping with mustard or linseed to reduce susceptibility to wilt and pod borer infestations."
        ]
    },
    "kidneybeans": {
        "name": "Kidney Beans (Phaseolus vulgaris)",
        "crop": "Kidney Beans",
        "icon": "🫘",
        "scientific": "Phaseolus vulgaris L.",
        "season": "Rabi / Zaid",
        "duration": "90 - 100 Days",
        "demand": "Medium",
        "price": "₹7,800 / Quintal",
        "fertilizer": "NPK complex (20:60:20 kg/ha) at planting. Supplement with foliar sprays of secondary nutrients during early flowering.",
        "tips": "Provide light and frequent irrigations. Keep the root zone well-aerated; waterlogging causes rapid yellowing and root rot.",
        "explanation": "Your soil parameters are ideal for short-duration legume crops. Kidney beans require mild temperatures and neutral to slightly acidic pH levels.",
        "sustainable_tips": [
            "Apply straw mulch to protect shallow roots from temperature fluctuations and retain moisture.",
            "Implement sprinkler irrigation to deliver uniform light watering and avoid soil compaction.",
            "Integrate organic neem cake in soil preparation to control root-knot nematodes naturally."
        ]
    },
    "pigeonpeas": {
        "name": "Pigeon Peas (Cajanus cajan)",
        "crop": "Pigeon Peas",
        "icon": "🫛",
        "scientific": "Cajanus cajan L. Millsp.",
        "season": "Kharif (Monsoon)",
        "duration": "150 - 180 Days",
        "demand": "High",
        "price": "₹7,000 / Quintal",
        "fertilizer": "Basal application of NPK (20:50:20 kg/ha). Treat seeds with Trichoderma viride to prevent fusarium wilt.",
        "tips": "Avoid waterlogging. Space plants wide apart as they develop a deep taproot system and a large canopy.",
        "explanation": "Chosen due to high temperature adaptability and tolerance to low-to-medium rainfall. It acts as an excellent soil rejuvenator through nitrogen fixation.",
        "sustainable_tips": [
            "Grow pigeon peas on raised ridges to ensure excess monsoon water drains away easily.",
            "Use the crop as a windbreak or border crop to protect main sensitive crops and reduce soil erosion.",
            "Harvest dry stalks for use as bio-fuel or composting materials, returning organic carbon to the farm."
        ]
    },
    "mothbeans": {
        "name": "Moth Beans (Vigna aconitifolia)",
        "crop": "Moth Beans",
        "icon": "🤎",
        "scientific": "Vigna aconitifolia (Jacq.) Marechal",
        "season": "Kharif (Monsoon)",
        "duration": "75 - 90 Days",
        "demand": "Medium",
        "price": "₹6,800 / Quintal",
        "fertilizer": "Very low fertilizer requirements. A light dose of Single Super Phosphate (SSP) at sowing is usually sufficient.",
        "tips": "Extremely drought-tolerant. Irrigation is needed only under prolonged dry spells during flowering.",
        "explanation": "Optimal for hyper-arid conditions with low rainfall and high temperatures. Moth beans grow well in poor, sandy soils where other crops fail.",
        "sustainable_tips": [
            "Use as a sand-stabilizing cover crop to prevent wind erosion in dry, arid regions.",
            "Incorporate residues back into the soil post-harvest to improve soil organic matter in drylands.",
            "Practice zero-tillage sowing to conserve seedbed moisture in arid zones."
        ]
    },
    "mungbean": {
        "name": "Mung Bean (Vigna radiata)",
        "crop": "Mung Bean",
        "icon": "💚",
        "scientific": "Vigna radiata L. Wilczek",
        "season": "Zaid (Summer)",
        "duration": "60 - 75 Days",
        "demand": "High",
        "price": "₹7,755 / Quintal",
        "fertilizer": "Basal application of NPK (15:40:20 kg/ha). Seed treatment with Rhizobium and PSB is highly recommended.",
        "tips": "Sow immediately after harvesting Rabi crops to utilize residual moisture. Protect from whitefly vector using yellow sticky traps.",
        "explanation": "Matches warm temperatures, moderate humidity, and quick turnaround requirements. It serves as a great catch crop between seasonal shifts.",
        "sustainable_tips": [
            "Practice intercropping with sugarcane or cotton to generate extra income and improve soil fertility.",
            "Use yellow sticky traps and neem oil sprays for eco-friendly pest management against sucking insects.",
            "Incorporate crop biomass as green manure immediately after pod picking to fertilize the next crop."
        ]
    },
    "blackgram": {
        "name": "Black Gram (Vigna mungo)",
        "crop": "Black Gram",
        "icon": "🖤",
        "scientific": "Vigna mungo L. Hepper",
        "season": "Kharif / Rabi",
        "duration": "75 - 90 Days",
        "demand": "High",
        "price": "₹6,600 / Quintal",
        "fertilizer": "NPK starter dose (20:40:20 kg/ha). Treat seeds with Ammonium Molybdate to boost nodulation in acidic soils.",
        "tips": "Provide one critical irrigation at the pod-filling stage. Keep soil loose and free from weeds in first 3 weeks.",
        "explanation": "Recommended for its suitability in loamy soils with moderate moisture. Black gram requires warm temperatures and thrives as a short-rotation pulse.",
        "sustainable_tips": [
            "Use line sowing instead of broadcasting to improve light interception and facilitate mechanical weeding.",
            "Apply foliar spray of 2% Urea at flowering to prevent early senescing and increase pod count.",
            "Perform seed inoculation with localized mycorrhiza strains to enhance phosphorus absorption."
        ]
    },
    "lentil": {
        "name": "Lentil (Lens culinaris)",
        "crop": "Lentil",
        "icon": "🫘",
        "scientific": "Lens culinaris Medik.",
        "season": "Rabi (Winter)",
        "duration": "110 - 130 Days",
        "demand": "High",
        "price": "₹6,000 / Quintal",
        "fertilizer": "Basal dose of NPK (20:40:0 kg/ha). Zinc application (15 kg/ha) helps in crop establishment.",
        "tips": "Highly sensitive to waterlogging. Ensure excellent drainage. Avoid nitrogen top-dressing as it delays maturity.",
        "explanation": "Fits perfectly in cold winter conditions with dry atmosphere. Lentil has low water requirements and adapts to a wide range of soil textures.",
        "sustainable_tips": [
            "Adopt seed treatment with Rhizobium leguminosarum to optimize natural nitrogen fixation.",
            "Deploy light sprinkler irrigation to avoid water ponding which causes root rot.",
            "Include lentil in rice-fallow rotations to restore soil microbial diversity and structure."
        ]
    },
    "pomegranate": {
        "name": "Pomegranate (Punica granatum)",
        "crop": "Pomegranate",
        "icon": "🍎",
        "scientific": "Punica granatum L.",
        "season": "Perennial (Harvests in Bahar cycles)",
        "duration": "2 - 3 Years (Fruiting)",
        "demand": "Very High",
        "price": "₹9,500 / Quintal",
        "fertilizer": "Well-composted farmyard manure (20kg/plant) mixed with NPK and micronutrients during the pruning phase.",
        "tips": "Adopt drip irrigation and regulate watering to prevent fruit cracking during dry wind cycles.",
        "explanation": "Recommended for semi-arid locations with warm temperatures, low humidity, and sandy loam soil profiles. Pomegranate yields premium returns on well-drained soils.",
        "sustainable_tips": [
            "Utilize drip irrigation coupled with fertigation to supply water and nutrients directly to the root zone, saving 40% water.",
            "Apply organic neem cake and bio-pesticides to manage bacterial blight disease sustainably.",
            "Use paper bags or nylon nets to wrap developing fruits, preventing pest damage without chemical spraying."
        ]
    },
    "banana": {
        "name": "Banana (Musa)",
        "crop": "Banana",
        "icon": "🍌",
        "scientific": "Musa acuminata Colla",
        "season": "Year-Round",
        "duration": "11 - 12 Months",
        "demand": "Very High",
        "price": "₹2,100 / Quintal",
        "fertilizer": "Heavy feeder of Potassium. Apply 200g Nitrogen, 50g Phosphorus, and 300g Potassium per plant in 4-6 split doses.",
        "tips": "Protect plants from high winds using windbreaks. Prop up heavy fruiting stems (propping) with bamboo poles to prevent breaking.",
        "explanation": "Matches warm, humid, tropical conditions with high potassium levels. Banana is a water-loving crop requiring continuous nutrition.",
        "sustainable_tips": [
            "Incorporate banana pseudostem waste back into the soil as organic compost or mulch to recycle potassium.",
            "Install drip lines under plastic mulch to prevent weed growth and reduce moisture evaporation.",
            "Utilize tissue-cultured disease-free planting material to prevent panama wilt and bunchy top virus epidemics."
        ]
    },
    "mango": {
        "name": "Mango (Mangifera indica)",
        "crop": "Mango",
        "icon": "🥭",
        "scientific": "Mangifera indica L.",
        "season": "Perennial (Summer Harvest)",
        "duration": "5 - 6 Years (Fruiting)",
        "demand": "Very High",
        "price": "₹6,000 / Quintal",
        "fertilizer": "Apply organic compost annually during winters. Supplement with Urea, Superphosphate, and Muriate of Potash based on canopy size.",
        "tips": "Restrict irrigation during the flowering phase to induce heavy bloom. Control mango hopper pests during early bud formation.",
        "explanation": "Mango thrives in deep, well-drained soils in regions with distinct wet and dry seasons. Warm dry summers are ideal for fruit ripening.",
        "sustainable_tips": [
            "Adopt high-density planting (HDP) to maximize land use efficiency and ease canopy management.",
            "Employ drip irrigation during early crop establishment and fruit growth stages to minimize water waste.",
            "Deploy pheromone traps to control fruit flies organically, eliminating chemical residue on fruits."
        ]
    },
    "grapes": {
        "name": "Grapes (Vitis vinifera)",
        "crop": "Grapes",
        "icon": "🍇",
        "scientific": "Vitis vinifera L.",
        "season": "Perennial (Spring Harvest)",
        "duration": "2 - 3 Years (Maturity)",
        "demand": "High",
        "price": "₹8,200 / Quintal",
        "fertilizer": "High Potassium and Nitrogen during vegetative phase. Add soluble Boron and Zinc to prevent flower drop.",
        "tips": "Practice meticulous winter pruning and train vines on Y-trellises for optimal sunlight penetration and airflow.",
        "explanation": "Grapes are recommended due to low-to-medium humidity, warm days, and cool nights. They require excellent drainage and thrive in sandy-loam soils.",
        "sustainable_tips": [
            "Grow cover crops like clover between vine rows to prevent soil erosion and improve organic matter.",
            "Practice deficit irrigation techniques to enhance fruit quality (sugar content) and save water.",
            "Apply Trichoderma bio-fungicide to control powdery mildew without leaving chemical residue on grapes."
        ]
    },
    "watermelon": {
        "name": "Watermelon (Citrullus lanatus)",
        "crop": "Watermelon",
        "icon": "🍉",
        "scientific": "Citrullus lanatus (Thunb.) Matsum. & Nakai",
        "season": "Zaid (Summer)",
        "duration": "80 - 90 Days",
        "demand": "High",
        "price": "₹1,200 / Quintal",
        "fertilizer": "NPK (60:40:40 kg/ha). Apply extra Nitrogen during early vine growth, and shift to Potassium as fruits set.",
        "tips": "Grow on sandy riverbeds or raised beds. Reduce watering 10 days before harvesting to increase sugar accumulation.",
        "explanation": "Excellent for sandy soils with low organic matter. Watermelon thrives under high temperatures, dry climate, and controlled drip irrigation.",
        "sustainable_tips": [
            "Use biodegradable plastic mulching sheet to conserve soil water and prevent fruit rot by avoiding soil contact.",
            "Encourage natural pollinators by planting bee-attracting flowers near the watermelon patches.",
            "Use drip irrigation lines underneath mulch to deliver precise water volume, avoiding fungal leaf diseases."
        ]
    },
    "muskmelon": {
        "name": "Muskmelon (Cucumis melo)",
        "crop": "Muskmelon",
        "icon": "🍈",
        "scientific": "Cucumis melo L.",
        "season": "Zaid (Summer)",
        "duration": "75 - 85 Days",
        "demand": "Medium",
        "price": "₹1,800 / Quintal",
        "fertilizer": "NPK balanced starter. Supplement with Calcium Nitrate foliar sprays to prevent blossom end rot.",
        "tips": "Provide regular irrigation until fruit maturity, then taper off. Avoid overhead watering to prevent downy mildew.",
        "explanation": "Recommended for summer farming where high solar radiation and low humidity are prevalent. Muskmelon demands well-drained sandy loam soil.",
        "sustainable_tips": [
            "Adopt drip fertigation to match nutrient supply with crop growth stages, minimizing nitrogen leaching.",
            "Intercrop with marigolds to deter root nematodes and attract beneficial pest predators.",
            "Implement straw mulching to keep fruits clean and reduce soil temperature spikes."
        ]
    },
    "apple": {
        "name": "Apple (Malus domestica)",
        "crop": "Apple",
        "icon": "🍎",
        "scientific": "Malus domestica Borkh.",
        "season": "Perennial (Autumn Harvest)",
        "duration": "4 - 5 Years (Fruiting)",
        "demand": "Very High",
        "price": "₹12,000 / Quintal",
        "fertilizer": "Organic compost combined with Nitrogen during active spring growth. Apply Calcium sprays to prevent bitter pit disorder.",
        "tips": "Demands temperate climates with sufficient winter chilling hours. Prune annually to maintain open center shapes.",
        "explanation": "Optimal for cool temperate regions with low temperatures and high humidity. Apples require acidic to neutral, deep organic-rich soil.",
        "sustainable_tips": [
            "Adopt organic codling moth control using pheromone mating disruption dispensers.",
            "Manage orchard floor vegetation by maintaining a grass cover to conserve soil organic carbon.",
            "Employ drip irrigation coupled with soil moisture sensors to optimize water application in hilly terrains."
        ]
    },
    "orange": {
        "name": "Orange (Citrus)",
        "crop": "Orange",
        "icon": "🍊",
        "scientific": "Citrus sinensis L.",
        "season": "Perennial (Harvesting Oct-Mar)",
        "duration": "4 - 5 Years (Fruiting)",
        "demand": "High",
        "price": "₹4,800 / Quintal",
        "fertilizer": "Micro-nutrient cocktail (Zinc, Manganese, Iron) applied to foliage. Supplement soil with bio-fertilizers and gypsum.",
        "tips": "Use drip irrigation to deliver moisture directly to the root zone. Mulching around the trunk helps conserve soil water and controls weeds.",
        "explanation": "Recommended due to moderate climate, high humidity, and neutral soil pH. Citrus trees demand well-aerated soils with moderate irrigation.",
        "sustainable_tips": [
            "Deploy biological control agents like predatory mites and ladybugs to suppress citrus psylla and scale pests.",
            "Adopt drip irrigation with micro-sprinklers to reduce water runoff in sloping citrus orchards.",
            "Apply green compost around the tree basin to boost microbial activity and improve zinc absorption."
        ]
    },
    "papaya": {
        "name": "Papaya (Carica papaya)",
        "crop": "Papaya",
        "icon": "🍈",
        "scientific": "Carica papaya L.",
        "season": "Year-Round",
        "duration": "9 - 10 Months",
        "demand": "High",
        "price": "₹2,500 / Quintal",
        "fertilizer": "Continuous feeder. Apply NPK complex (50:50:50 g/plant) every two months. Add Boron to avoid fruit bumpiness.",
        "tips": "Extremely sensitive to waterlogging; even 24 hours of standing water can cause root rot. Grow on raised mounds.",
        "explanation": "Recommended for tropical zones with high temperatures and moderate humidity. Papaya grows fast and thrives in sandy loam soils.",
        "sustainable_tips": [
            "Grow on raised beds of 30-45 cm height to ensure absolute drainage during sudden rainfall events.",
            "Intercrop with short-duration vegetables during the first 3 months to maximize space and control weed growth.",
            "Construct wind barriers around the papaya block to protect plants from wind damage and stem breakage."
        ]
    },
    "coconut": {
        "name": "Coconut (Cocos)",
        "crop": "Coconut",
        "icon": "🥥",
        "scientific": "Cocos nucifera L.",
        "season": "Perennial",
        "duration": "6 - 7 Years (Maturity)",
        "demand": "High",
        "price": "₹3,800 / 100 Nuts",
        "fertilizer": "Apply 500g N, 320g P, and 1200g K per palm tree annually, along with 50kg farmyard manure. Add common salt (1kg/palm) to improve yield.",
        "tips": "Grows best in sandy, red sandy loams, or alluvial soils. Excavate wide basins around the palm base to capture rainwater.",
        "explanation": "Perfect match for coastal/tropical zones with high humidity, high rainfall, and sandy soils. Coconut trees are highly tolerant to salinity.",
        "sustainable_tips": [
            "Implement multi-tier cropping by growing cocoa, black pepper, or turmeric under coconut plantations to optimize solar radiation.",
            "Recycle coconut husks in trenches around the tree basin to act as natural sponges for water retention during dry seasons.",
            "Deploy green pheromone traps to manage rhinoceros beetle populations without synthetic pesticide spraying."
        ]
    },
    "cotton": {
        "name": "Cotton (Gossypium)",
        "crop": "Cotton",
        "icon": "☁️",
        "scientific": "Gossypium hirsutum L.",
        "season": "Kharif (Monsoon)",
        "duration": "165 - 180 Days",
        "demand": "Very High",
        "price": "₹7,020 / Quintal",
        "fertilizer": "Split nitrogen applications to sync with boll formation. Add Muriate of Potash (MOP) to improve fiber strength and pest resistance.",
        "tips": "Keep field weed-free during the critical first 60 days. Monitor for pink bollworm, and use pheromone traps.",
        "explanation": "Optimal for black cotton soil (regur) with moderate rainfall. Cotton requires warm temperatures, high solar radiation, and low humidity during ripening.",
        "sustainable_tips": [
            "Adopt Integrated Pest Management (IPM) using border crops of castor and cowpeas to attract pests away from cotton.",
            "Incorporate cotton crop residues back into the soil post-harvest using rotavators to restore organic carbon.",
            "Implement high-density planting system (HDPS) to achieve uniform maturity and ease mechanical harvesting."
        ]
    },
    "jute": {
        "name": "Jute (Corchorus)",
        "crop": "Jute",
        "icon": "🌾",
        "scientific": "Corchorus olitorius L.",
        "season": "Kharif (Monsoon)",
        "duration": "120 - 140 Days",
        "demand": "High",
        "price": "₹5,050 / Quintal",
        "fertilizer": "NPK (40:20:20 kg/ha). Apply Urea as a top-dressing after weeding. Organic compost increases fiber quality.",
        "tips": "Demands hot and humid climates. Retting (soaking stalks in slow water for 15-20 days) is critical for fiber extraction.",
        "explanation": "Jute is recommended due to high temperature, high humidity, and high rainfall conditions. It grows best in rich alluvial soils of river basins.",
        "sustainable_tips": [
            "Perform water retting in slow-flowing clean water streams rather than stagnant pools to maintain fiber quality and prevent local pollution.",
            "Utilize ribbon retting technology to reduce water usage by 60% and improve fiber recovery.",
            "Incorporate jute leaves as organic manure since they decompose rapidly and enrich the soil with organic matter."
        ]
    },
    "coffee": {
        "name": "Coffee (Coffea)",
        "crop": "Coffee",
        "icon": "☕",
        "scientific": "Coffea arabica L.",
        "season": "Perennial (Monsooned)",
        "duration": "3 - 4 Years (Maturity)",
        "demand": "High",
        "price": "₹16,500 / Quintal",
        "fertilizer": "Well-decomposed organic manure supplemented with NPK formulation (90:45:90 kg/ha). Apply Zinc and Boron foliar sprays annually.",
        "tips": "Maintain 30-40% filter shade over coffee shrubs using shade trees like Silver Oak. Regular pruning keeps tree architecture optimal.",
        "explanation": "Recommended for high-altitude hilly tracts with mild temperatures, high rainfall, and acidic soils. Coffee requires well-drained organic soils.",
        "sustainable_tips": [
            "Practice shade-grown coffee agroforestry to preserve biodiversity and protect coffee plants from microclimate extremes.",
            "Establish contour bunds and vegetative vetiver barriers to prevent soil wash-off in hilly coffee slopes.",
            "Recycle coffee pulp waste after fermentation by composting it into high-quality organic fertilizer for the estate."
        ]
    }
}

def get_crop_data(crop_label):
    """
    Retrieves crop details, falling back to a default structure if the crop label is unknown.
    """
    label_lower = crop_label.lower().strip().replace(" ", "")
    # Handle minor variations in names
    if "kidney" in label_lower:
        label_key = "kidneybeans"
    elif "pigeon" in label_lower:
        label_key = "pigeonpeas"
    elif "moth" in label_lower:
        label_key = "mothbeans"
    elif "mung" in label_lower:
        label_key = "mungbean"
    elif "blackgram" in label_lower:
        label_key = "blackgram"
    else:
        label_key = label_lower
        
    if label_key in CROP_DETAILS_DB:
        return CROP_DETAILS_DB[label_key]
        
    # Default fallback
    name_title = crop_label.title()
    return {
        "name": f"{name_title} (Specie)",
        "crop": name_title,
        "icon": "🌱",
        "scientific": f"{name_title} spp.",
        "season": "Seasonal",
        "duration": "90 - 120 Days",
        "demand": "Medium",
        "price": "Market Rate",
        "fertilizer": "Apply balanced NPK fertilizer based on standard local soil testing recommendations.",
        "tips": "Keep soil aerated and watered during critical growth stages. Consult local agronomy services for optimal yield.",
        "explanation": "Matches the environmental conditions calculated by the Random Forest classifier model.",
        "sustainable_tips": [
            "Use organic composting and vermicomposting to build soil structure.",
            "Employ drip irrigation to conserve water and prevent nutrient leaching.",
            "Adopt rotation with nitrogen-fixing legume crops to restore soil health."
        ]
    }
