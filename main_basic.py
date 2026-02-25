from sentinel_suite import SentinelSuite
from colorama import Fore, Style, init

init(autoreset=True)


def run():
    suite = SentinelSuite()
    intent = "Create a secure Docker environment for a Python app and Postgres DB."

    print(f"{Fore.CYAN}🚀 STARTING BASIC MODE...")
    design, report = suite.run_cycle(intent)

    print(f"\n🛡️ AUDITOR REPORT:\n{report}")
    print(f"\n{Fore.GREEN}✅ Infrastructure generated in /output")


if __name__ == "__main__":
    run()
