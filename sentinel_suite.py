from architect.architect import SentinelArchitect
from auditor.auditor import SentinelAuditor


class SentinelSuite:
    def __init__(self):
        self.architect = SentinelArchitect()
        self.auditor = SentinelAuditor()

    def run_cycle(self, intent, previous_report=None):
        if previous_report:
            prompt = f"REGENERATE FOLLOWING THIS AUDIT FEEDBACK:\n{previous_report}\n\nORIGINAL INTENT:\n{intent}"
        else:
            prompt = intent

        design = self.architect.generate_infrastructure(prompt)
        generated_code = design.files[0].content

        audit_report = self.auditor.audit_text(intent, generated_code)

        return design, audit_report
