TENDER_DATASET = {
    "websites": [
        {
            "name": "eProcurement System of India",
            "base_url": "https://eprocure.gov.in",
            "specializations": [
                "government projects",
                "infrastructure",
                "construction",
                "IT services",
                "defense",
                "healthcare"
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
            "name": "Tender Detail",
            "base_url": "https://www.tenderdetail.com",
            "specializations": [
                "public tenders",
                "private tenders",
                "state government tenders",
                "central government tenders",
                "healthcare"
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
            "base_url": "https://www.bidassist.com",
            "specializations": [
                "infrastructure",
                "healthcare",
                "medical equipment",
                "IT services"
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
            "name": "Tender247",
            "base_url": "https://www.tender247.com",
            "specializations": [
                "construction",
                "healthcare",
                "medical supplies",
                "IT services"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "bids", "contracts"]
            },
            "geographical_coverage": ["India"],
            "api_available": True
        },
        {
            "name": "National Tenders",
            "base_url": "https://www.nationaltenders.com",
            "specializations": [
                "eProcurement",
                "public tenders",
                "healthcare"
            ],
            "features": {
                "search_supported": True,
                "update_frequency": "daily",
                "document_types": ["tenders", "projects", "contracts"]
            },
            "geographical_coverage": ["India"],
            "api_available": False
        }
    ],
    "keywords_mapping": {
        "medical equipment": ["medical supplies", "healthcare", "medical devices", "hospital equipment"],
        "construction": ["building", "infrastructure", "civil works", "roads"],
        "IT services": ["software", "hardware", "digital", "technology"],
        "healthcare": ["medical", "hospital", "pharmaceutical", "health"],
        "defense": ["military", "security", "weapons", "ammunition"],
        "education": ["schools", "colleges", "training", "e-learning"],
        "agriculture": ["farming", "irrigation", "seeds", "fertilizers"],
        "oil and gas": ["petroleum", "natural gas", "refineries", "pipelines"]
    }
}
