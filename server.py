
from fastmcp import FastMCP

from tools import (
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    get_total_credit_hours,
    save_report,
    send_notification,
    tavily_web_search
)

mcp = FastMCP("cgpa")


mcp.tool(marks_to_grade_points)
mcp.tool(calculate_semester_gpa)
mcp.tool(calculate_new_cgpa)
mcp.tool(required_gpa_for_target)
mcp.tool(get_semester_courses)
mcp.tool(get_remaining_credit_hours)
mcp.tool(get_total_credit_hours, name="get_credit_hours")
mcp.tool(save_report)
mcp.tool(send_notification)
mcp.tool(tavily_web_search)



if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=port
    )

