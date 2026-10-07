# case_g6

XSS remediation verified

After Q2's penetration test found reflected and stored XSS in the customer portal, we replaced our ad-hoc escaping with the sanitiser library across all templates and shipped on 14 June. Verification: our DAST scanner has run nightly against staging and production since 15 June, with zero XSS findings across 1,100+ pages; SAST reports no dangerous sink patterns in the new template layer. Our internal application-security team, which wrote the sanitiser integration, also re-ran the original Q2 exploit payloads by hand against the affected endpoints, and all are now blocked. The scanner's XSS module uses a large payload corpus and we have no reason to doubt its coverage. Bug-bounty payouts for XSS fell from four in the first half of the year to zero since the change, and no new XSS tickets have been filed by support in six weeks. On this basis we are closing the XSS workstream, reassigning the team, and recommending the same library to the platform team for the internal tools estate.

Task: before this claim is accepted, what must be questioned or tested?
