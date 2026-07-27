from collections import defaultdict

def build_report(advisories):
    critical = []
    high = []
    exploited = []
    services = []
  
    for advisory in advisories:
        if advisory.source in {
            "AWS",
            "Cloudflare",
            "Anthropic",
        }:
            services.append(advisory)
            continue

        if advisory.exploited:
            exploited.append(advisory)
            continue

        if advisory.severity == "CRITICAL":
            critical.append(advisory)
        elif advisory.severity == "HIGH":
            high.append(advisory)

    lines = []
    lines.append("🛡 DEVOPS SECURITY DIGEST")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━")

    if critical:
        lines.append("")
        lines.append("🚨 CRITICAL")
        lines.append("")

        for item in critical:
            lines.append(f"• {item.product}")
            if item.cve:
                lines.append(f"  {item.cve}")
            lines.append(f"  {item.title}")

            if item.score:
                lines.append(f"  CVSS {item.score}")

            if item.action:
                lines.append(f"  Action: {item.action}")
            lines.append("")

    if high:
        lines.append("⚠ HIGH")
        lines.append("")
        for item in high:
            lines.append(f"• {item.product}")
            lines.append(f"  {item.title}")
            lines.append("")

    if exploited:
        lines.append("🔥 KNOWN EXPLOITED")
        lines.append("")
        for item in exploited:
            lines.append(f"• {item.cve}")
            lines.append(f"  {item.product}")
            lines.append("")
    lines.append("☁ PLATFORM STATUS")
    lines.append("")
  
    if not services:
        lines.append("✅ No reported incidents")

    else:
        for item in services:
            lines.append(f"⚠ {item.title}")
    lines.append("")
    lines.append("━━━━━━━━━━━━━━━━━━━━━━")
    lines.append("")
    lines.append("Summary")
    lines.append(f"Critical : {len(critical)}")
    lines.append(f"High : {len(high)}")
    lines.append(f"Known Exploited : {len(exploited)}")
    lines.append(f"Platform Incidents : {len(services)}")

    return "\n".join(lines)
