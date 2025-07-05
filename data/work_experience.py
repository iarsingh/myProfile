from datetime import datetime

WORK_EXPERIENCE = [
    {
        "title": "Consultant",
        "company": "Capgemini",
        "location": "Navi Mumbai",
        "start_date": datetime(2024, 9, 1),
        "end_date": None,  # Present
        "duration": "Sept 2024 - Present",
        "description": [
            "Spearheading CI/CD pipeline implementation using Jenkins, GitLab CI, and Azure DevOps to automate builds, tests, and deployments across hybrid and GCP-centric cloud environments",
            "Managing containerized application deployments using Kubernetes and Docker, ensuring high availability and scalability",
            "Automating infrastructure provisioning and configuration with Terraform and Ansible for Google Cloud Platform (GCP), optimizing cloud resource management and cost-efficiency",
            "Implementing monitoring and logging solutions using the ELK Stack and Stream Security for proactive issue resolution, security compliance, and threat detection",
            "Collaborating with cross-functional teams to align DevOps practices with application development, QA, and business goals",
            "Supporting disaster recovery and backup strategies using Veeam and Kasten K10 to ensure business continuity",
            "Actively contributing to Full Stack development initiatives with Java and Spring Boot, while upskilling in React and Node.js",
            "Exploring MLOps practices, including automated model deployment pipelines and MLflow integration, to support scalable, intelligent system workflows"
        ],
        "skills": ["Jenkins", "GitLab CI", "Azure DevOps", "Kubernetes", "Docker", "Terraform", "Ansible", "GCP", "ELK Stack", "MLflow", "Java", "React", "Node.js"]
    },
    {
        "title": "Senior Software Engineer",
        "company": "Tech Mahindra Pvt. Ltd.",
        "location": "Mumbai",
        "start_date": datetime(2022, 7, 1),
        "end_date": datetime(2024, 8, 31),
        "duration": "Jul 2022 - Aug 2024",
        "description": [
            "Designed and implemented CI/CD pipelines using Jenkins, Bitbucket, and GitHub, integrating Terraform, Kubernetes, Docker, Helm, and Ansible for scalable DevOps workflows",
            "Deployed microservices to Kubernetes clusters using Helm Charts and Docker images, streamlining and standardizing application deployment processes",
            "Integrated SAST and DAST security tools into Jenkins pipelines to enforce secure coding practices through automated vulnerability scanning",
            "Built Infrastructure as Code solutions using Terraform for consistent infrastructure provisioning across GCP, Azure, AWS",
            "Led system security and SIEM management initiatives, including the integration of Prisma for real-time threat monitoring",
            "Developed robust monitoring and alerting systems using the ELK Stack and custom scripts, enabling real-time performance tracking and rapid issue resolution",
            "Engineered comprehensive backup and disaster recovery strategies using Veeam, Kasten K10, and Terraform, ensuring business continuity across multi-cloud environments",
            "Collaborated closely with cloud vendor teams (Google, Microsoft, AWS) to resolve escalated issues and optimize platform-specific infrastructure",
            "Automated OS patching and configuration management for Windows and Linux instances across GCP, Azure, and AWS",
            "Supported full stack development and MLOps adoption initiatives within internal teams by contributing DevOps automation for app deployment and ML experimentation environments"
        ],
        "skills": ["Jenkins", "Bitbucket", "GitHub", "Terraform", "Kubernetes", "Docker", "Helm", "Ansible", "SAST", "DAST", "Prisma", "ELK Stack", "Veeam", "Kasten K10", "AWS", "Azure", "GCP"]
    },
    {
        "title": "System Engineer",
        "company": "TCS",
        "location": "India",
        "start_date": datetime(2021, 7, 1),
        "end_date": datetime(2022, 7, 31),
        "duration": "Jul 2021 - Jul 2022",
        "description": [
            "Orchestrated CI/CD pipelines using Jenkins, Git, GitHub, and Google Cloud Build to ensure efficient, automated, and reliable application delivery within GCP environments",
            "Led the migration of on-premises databases to Google Cloud SQL, ensuring minimal downtime, data integrity, and seamless performance post-transition",
            "Designed and deployed scalable containerized solutions using Docker and Kubernetes (GKE), enhancing application reliability and resource efficiency",
            "Built & maintained native CI/CD pipelines for container-based deployments, reducing manual intervention and accelerating release cycles",
            "Hosted and managed applications on GCP, utilizing GKE, Compute Engine, Cloud SQL, and related services for scalable, production-grade deployment",
            "Facilitated internal upskilling through mentorship sessions and knowledge-sharing meetings, fostering team collaboration and DevOps adoption"
        ],
        "skills": ["Jenkins", "Git", "GitHub", "Google Cloud Build", "GCP", "Cloud SQL", "Docker", "Kubernetes", "GKE", "Compute Engine"]
    },
    {
        "title": "Assistant System Engineer",
        "company": "TCS",
        "location": "India",
        "start_date": datetime(2019, 9, 1),
        "end_date": datetime(2021, 7, 31),
        "duration": "Sept 2019 - Jul 2021",
        "description": [
            "Resolved post-deployment production issues within defined SLAs, ensuring system stability and minimal business impact",
            "Maintained & supported cloud-hosted Java applications integrated with Azure and Jenkins-based CI/CD pipelines",
            "Designed and implemented automated deployment workflows for cloud-native applications, reducing manual efforts and increasing deployment consistency",
            "Collaborated with cloud service providers to resolve infrastructure challenges and enhance system performance"
        ],
        "skills": ["Java", "Azure", "Jenkins", "CI/CD", "Cloud Applications", "Production Support"]
    }
]
