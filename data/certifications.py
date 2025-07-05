"""
Certification data for Akhilesh Singh's professional portfolio
"""

CERTIFICATIONS = [
    {
        "name": "Professional Cloud DevOps Engineer Certification",
        "issuer": "Google Cloud",
        "year": "2025",
        "status": "Active",
        "description": "Advanced certification demonstrating expertise in DevOps practices on Google Cloud Platform"
    },
    {
        "name": "Executive Post Graduate Certification in Cloud Computing",
        "issuer": "Academic Institution",
        "year": "2024",
        "status": "Completed",
        "description": "Comprehensive program covering cloud computing fundamentals, architecture, and implementation"
    },
    {
        "name": "Google Cloud Associate Engineer",
        "issuer": "Google Cloud",
        "year": "2024",
        "status": "Active",
        "description": "Validates ability to deploy applications, monitor operations, and maintain cloud projects on GCP"
    },
    {
        "name": "Designing and Implementing Microsoft DevOps Solutions",
        "issuer": "Microsoft",
        "year": "2024",
        "status": "Active",
        "description": "Demonstrates skills in implementing DevOps practices using Microsoft technologies and Azure DevOps"
    },
    {
        "name": "AWS Certified Solutions Architect – Associate",
        "issuer": "Amazon Web Services",
        "year": "2022",
        "status": "Active",
        "description": "Validates expertise in designing distributed systems and applications on AWS platform"
    }
]

# Additional certification details
CERTIFICATION_CATEGORIES = {
    "Cloud Platforms": ["Google Cloud Associate Engineer", "AWS Certified Solutions Architect – Associate"],
    "DevOps": ["Professional Cloud DevOps Engineer Certification", "Designing and Implementing Microsoft DevOps Solutions"],
    "Education": ["Executive Post Graduate Certification in Cloud Computing"]
}

# Certification statistics
CERTIFICATION_STATS = {
    "total_certifications": len(CERTIFICATIONS),
    "active_certifications": len([cert for cert in CERTIFICATIONS if cert["status"] == "Active"]),
    "cloud_providers": 3,  # AWS, Azure, GCP
    "latest_year": 2025
}
