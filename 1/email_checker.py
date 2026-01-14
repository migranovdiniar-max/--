import sys
import dns.resolver
import dns.exception

def check_email_domain(email):
    try:
        domain = email.split('@')[1]
    except IndexError:
        return "домен отсутствует"
    
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        if mx_records:
            return "домен валиден"
        else:
            return "MX-записи отсутствуют или некорректны"
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
        return "домен отсутствует"
    except dns.exception.DNSException:
        return "MX-записи отсутствуют или некорректны"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python email_checker.py email1@example.com email2@example.com ...")
        sys.exit(1)
    
    emails = sys.argv[1:]
    for email in emails:
        status = check_email_domain(email)
        print(f"{email}: {status}")