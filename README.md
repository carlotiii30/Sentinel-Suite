# Sentinel Security Suite 🛡️🏗️
*(The AI-Driven Lifecycle for Automated Cloud Governance)*

Sentinel Security Suite is an integrated DevSecOps ecosystem designed to close the "translation gap" between high-level administrative security policies and hardened technical implementations. By orchestrating two specialized AI agents, the suite manages the full security lifecycle: from Security-by-Design generation to Detective Control auditing.

---

## 🛰️ The Sentinel Ecosystem
This suite integrates two modular projects into a unified security pipeline:
* **[Sentinel Auditor](https://github.com/carlotiii30/Sentinel-Auditor)**: Detective control that audits existing configurations.
* **[Sentinel Architect](https://github.com/carlotiii30/Sentinel-Architect)**: Preventive control that generates secure IaC from natural language.

---

## 🌟 Inspiration: Adversarial Security

The core architecture of this suite is directly inspired by my Bachelor's Thesis (TFG) research on Generative Adversarial Networks (GANs).
In this ecosystem:
* **The Generator (Architect)**: Attempts to create functional and secure infrastructure.
* **The Discriminator (Auditor)**: Challenges the generator's output against strict security standards (CIA Triad, Least Privilege).

This "adversarial" relationship creates a continuous feedback loop where the Auditor identifies vulnerabilities (Discriminator) to ensure the Architect (Generator) produces production-ready, compliant code.

## 🚀 Key Features

* **Closed-Loop Governance**: A single workflow from human intent → code generation → security verification.
* **ISC2 CC Standardized**: Every audit report and architectural decision is grounded in the CIA Triad, Defense in Depth, and Least Privilege principles.
* **Automated Hardening**: Generates Docker and Docker Compose files with embedded Security Rationales explaining the "why" behind every measure.
* **Transparent Remediation**: High-readability reports that don't just find bugs, but explain the risk and provide the exact technical fix.

## 🛠️ Technical Stack

- **Language:** Python 3.10+
- **AI Orchestration:** LangChain
- **LLM Integration:** **Google Gemini (2.5 Flash)** via Google AI Studio 🚀
- **Security Framework:** Grounded in **ISC2 CC** standards.
- **Dependency Management**: Poetry.

## 📖 How it Works

1. **Define Intent**: Provide a requirement (e.g., "Create a web app with a private DB using environment variables for secrets").
2. **AI Architecting**: Sentinel-Architect generates the hardened IaC files in the /output folder.
3. **Cross-Verification**: Sentinel-Auditor automatically ingests the generated code and compares it against the original security intent.
4. **Final Verdict**: The suite produces a Compliance Report. If the Architect took insecure shortcuts, the Auditor will flag them and demand a remediation.

## 👷🏼 Installation & Setup

1. Clone the suite and its sub-packages:
2. Install dependencies.
3. Configure Environment: Create a .env file with your GOOGLE_API_KEY.
4. Run the Integrated Demo.

---

## 🔍 Future Roadmap
- **Auto-Fix Mode**: Implementation of a convergence loop where the Architect automatically fixes code based on Auditor feedback.
- **Cloud Native Support**: Expansion to Terraform (AWS/Azure) templates and Kubernetes manifests.
  
---

> _This project validates the competencies acquired in the **ISC2 Certified in Cybersecurity (CC)** program (Completed Feb 2026)._
