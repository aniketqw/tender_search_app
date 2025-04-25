TENDER_DATASET = {
    "websites": [
        {
            "name": "eProcurement System of India",
            "base_url": "https://eprocure.gov.in/cppp/",
            "specializations": ["government projects", "infrastructure", "construction", "IT services", "healthcare"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["RFP", "RFQ", "EOI", "tender notices"]
            }
        },
        {
            "name": "Government e-Marketplace",
            "base_url": "https://gem.gov.in/",
            "specializations": ["government procurement", "goods", "services"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["bids", "contracts"]
            }
        },
        {
            "name": "BidAssist",
            "base_url": "https://bidassist.com/",
            "specializations": ["infrastructure", "healthcare", "IT services"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "projects"]
            }
        },
        {
            "name": "Development Aid",
            "base_url": "https://www.developmentaid.org/",
            "specializations": ["development projects", "NGO projects"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "grants"]
            }
        },
        {
            "name": "Asian Development Bank",
            "base_url": "https://selfservice.adb.org/OA_HTML/adb/adbpos/jsp/ADBCMSHomepage.jsp",
            "specializations": ["development projects", "infrastructure"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "contracts"]
            }
        },
        {
            "name": "World Bank",
            "base_url": "https://projects.worldbank.org/en/projects-operations/procurement",
            "specializations": ["development projects", "infrastructure"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "notices"]
            }
        },
        {
            "name": "UNDP",
            "base_url": "https://www.undp.org/procurement",
            "specializations": ["development projects", "humanitarian"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["procurement notices", "EOIs"]
            }
        },
        {
            "name": "NGO Box",
            "base_url": "https://www.ngobox.org/",
            "specializations": ["NGO projects", "social sector"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["RFPs", "EOIs"]
            }
        },
        {
            "name": "DevNet Jobs",
            "base_url": "https://www.devnetjobs.org/",
            "specializations": ["development projects", "NGO jobs"],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["RFPs", "tenders"]
            }
        }
    ],
    "keywords_mapping": {
        "construction": [
            "civil works", "infrastructure", "building", "roads", "bridges",
            "construction materials", "renovation", "architectural", "structural"
        ],
        "healthcare": [
            "medical equipment", "hospital supplies", "pharmaceuticals", "diagnostic",
            "surgical instruments", "laboratory equipment", "healthcare services"
        ],
        "IT_services": [
            "software development", "hardware", "networking", "cybersecurity",
            "cloud computing", "digital transformation", "IT infrastructure"
        ],
        "education": [
            "educational equipment", "school supplies", "training", "e-learning",
            "educational software", "teaching materials"
        ],
        "agriculture": [
            "farming equipment", "irrigation", "seeds", "fertilizers", "agricultural machinery",
            "crop management", "agricultural supplies"
        ],
        "energy": [
            "power generation", "renewable energy", "solar", "wind", "electricity",
            "energy efficiency", "power distribution"
        ],
        "environment": [
            "waste management", "water treatment", "pollution control",
            "environmental services", "recycling"
        ]
    }
}
