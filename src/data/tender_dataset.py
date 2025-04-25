TENDER_DATASET = {
    "websites": [
        {
            "name": "eProcurement System of India (CPPP)",
            "base_url": "https://eprocure.gov.in/cppp/",
            "specializations": [
                "government projects", "infrastructure", "construction", 
                "IT services", "defense", "healthcare", "skill development",
                "carbon emissions", "monitoring", "evaluation"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["RFP", "RFQ", "EOI", "tender notices"]
            },
            "geographical_coverage": ["India"],
            "api_available": False
        },
        {
            "name": "Government e-Marketplace (GeM)",
            "base_url": "https://gem.gov.in/",
            "specializations": [
                "government procurement", "IT services", "healthcare", "training",
                "consultancy", "research", "surveys", "studies"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "contracts", "awards"]
            },
            "geographical_coverage": ["India"],
            "api_available": True
        },
        {
            "name": "BidAssist",
            "base_url": "https://bidassist.com/",
            "specializations": [
                "infrastructure", "healthcare", "medical equipment", "IT services",
                "carbon neutrality", "sustainability", "research"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "projects", "contracts"]
            },
            "geographical_coverage": ["India"],
            "api_available": True
        },
        {
            "name": "Development Aid",
            "base_url": "https://www.developmentaid.org/",
            "specializations": [
                "development projects", "social audit", "impact assessment",
                "sustainability", "monitoring and evaluation"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "grants", "RFPs"]
            },
            "geographical_coverage": ["Global", "India"],
            "api_available": True
        },
        {
            "name": "Asian Development Bank (ADB)",
            "base_url": "https://selfservice.adb.org/OA_HTML/adb/adbpos/jsp/ADBCMSHomepage.jsp",
            "specializations": [
                "development projects", "infrastructure", "sustainability",
                "climate neutrality", "evaluation studies"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "consulting opportunities"]
            },
            "geographical_coverage": ["Asia", "India"],
            "api_available": True
        },
        {
            "name": "World Bank Procurement",
            "base_url": "https://projects.worldbank.org/en/projects-operations/procurement",
            "specializations": [
                "development projects", "infrastructure", "education",
                "healthcare", "sustainability", "research"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "weekly",
                "document_types": ["tenders", "contracts", "RFPs"]
            },
            "geographical_coverage": ["Global", "India"],
            "api_available": True
        },
        {
            "name": "UNDP Procurement Notices",
            "base_url": "https://procurement-notices.undp.org/",
            "specializations": [
                "development projects", "sustainability", "impact studies",
                "capacity building", "climate neutrality"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["procurement notices", "RFPs", "EOIs"]
            },
            "geographical_coverage": ["Global", "India"],
            "api_available": True
        },
        {
            "name": "NGO Box",
            "base_url": "https://ngobox.org/rfp_eoi_listing.php",
            "specializations": [
                "social sector", "NGOs", "impact assessment", "research",
                "monitoring and evaluation", "training"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "weekly",
                "document_types": ["RFPs", "EOIs"]
            },
            "geographical_coverage": ["India"],
            "api_available": False
        },
        {
            "name": "DevNet Jobs",
            "base_url": "https://www.devnetjobsindia.org/rfp_assignments.aspx",
            "specializations": [
                "development sector", "research", "impact studies",
                "capacity building", "monitoring and evaluation"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "weekly",
                "document_types": ["RFPs", "Tenders", "Assignments"]
            },
            "geographical_coverage": ["India"],
            "api_available": False
        }
    ],
    "keywords_mapping": {
        "consultancy": ["Consultancy Firm", "Consultant Firm", "Hiring of Consultants", "Selection Of Consultancy Firm", "Selection of Consulting Agency", "Management Consultants"],
        "research": ["Research", "Research study", "Market Research", "Market survey", "studies", "study", "analysis"],
        "sustainability": ["Sustainability evaluation", "Carbon Neutrality", "Climate neutrality", "Carbon emissions assessment", "Carbon footprint analysis", "Carbon offset evaluation", "Net zero emissions", "Net-zero carbon", "Low-carbon strategy", "Emission reduction monitoring", "Environmental performance monitoring"],
        "capacity_building": ["capacity building", "Training & Capacity Building", "Learning & Development", "Training", "Training Effectiveness Evaluation", "Competency Development", "Skill development", "Skill Gap analysis", "Skill Gap", "Skill Consulting"],
        "monitoring_evaluation": ["Monitoring & Evaluation", "M&E", "Performance Monitoring", "Evaluation Study", "Evaluation study", "Baseline study", "Endline Study", "Social Audit", "monitoring and evaluation", "impact assessment", "impact study"],
        "project_management": ["PMU", "PMC", "PIU", "Implementation Of PMU", "Implementation Of Program Management Unit", "Project management unit", "Project Monitoring unit", "Preparation Of Project Operation", "Project Operation Manual"],
        "data_collection": ["Data Collection", "Survey", "Survey Works", "Survey and Investigation services", "Surveys", "Tracer study"],
        "health": ["Health", "Health Consulting", "Healthcare Services", "Digital health"],
        "assessments": ["Need Assessments", "Capacity Assessment", "TSA", "Subject Matter Experts"],
        "financial": ["Financial Literacy Training", "IEC"],
        "technical_services": ["technical support", "technical support agency"],
        "construction_engineering": ["Quantity Survey", "Manpower"],
        "payment_models": ["Per Person Per Month Based", "Milestone/Deliverable Based"]
    }
}