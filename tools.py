MD = {"MD-001", "MD-002"}  

COURSES = {
    1: [
        ("MS-251", "Probability & Statistics", 3.0),
        ("GE-160", "Applications of ICT", 3.0),
        ("GE-169", "Applied Physics", 3.0),
        ("GE-167", "Discrete Structures", 3.0),
        ("HQ-001", "Quran Translation - I", 0.5),
        ("GE-190", "Functional English", 3.0),
    ],
    2: [
        ("CC-112", "Programming Fundamentals", 3.0),
        ("CC-112-L", "Programming Fundamentals Lab", 1.0),
        ("CC-110", "Digital Logic Design", 2.0),
        ("CC-110-L", "Digital Logic Design Lab", 1.0),
        ("MS-252", "Linear Algebra", 3.0),
        ("GE-191", "Expository Writing", 3.0),
        ("GE-163", "Islamic Studies", 2.0),
        ("HQ-002", "Quran Translation - II", 0.5),
    ],
    3: [
        ("CC-211", "Object Oriented Programming", 3.0),
        ("CC-211-L", "Object Oriented Programming Lab", 1.0),
        ("CC-215", "Database Systems", 3.0),
        ("CC-215-L", "Database Systems Lab", 1.0),
        ("CC-210", "Computer Organization & Assembly Language", 3.0),
        ("GE-162", "Calculus & Analytical Geometry", 3.0),
        ("GE-192", "Introduction to Management", 2.0),
        ("HQ-003", "Quran Translation - III", 0.5),
    ],
    4: [
        ("CC-213", "Data Structures", 3.0),
        ("CC-213-L", "Data Structures Lab", 1.0),
        ("CC-312", "Information Security", 3.0),
        ("CC-214", "Computer Networks", 3.0),
        ("CC-212", "Software Engineering", 3.0),
        ("DC-220", "Advanced Database Management Systems", 3.0),
        ("HQ-004", "Quran Translation - IV", 0.5),
    ],
    5: [
        ("CC-313", "Analysis of Algorithms", 3.0),
        ("CC-310", "Artificial Intelligence", 3.0),
        ("DC-320", "Theory of Automata and Formal Languages", 3.0),
        ("DC-321", "Human Computer Interaction", 3.0),
        ("DC-322", "Computer Architecture", 3.0),
        ("EC-330", "Web Technologies / Elective", 3.0),
        ("HQ-005", "Quran Translation - V", 0.5),
    ],
    6: [
        ("CC-311", "Operating Systems", 3.0),
        ("EC-333", "Mobile Application Development / Elective", 3.0),
        ("EC-324", "Software Construction & Development / Elective", 3.0),
        ("EC-335", "Machine Learning / Elective", 3.0),
        ("EC-334", "Game Design and Development / Elective", 3.0),
        ("MS-253", "Multivariable Calculus", 3.0),
        ("HQ-006", "Quran Translation - VI", 0.5),
    ],
    7: [
        ("CC-411", "Final Year Project - I", 3.0),
        ("DC-328", "Parallel & Distributed Computing", 3.0),
        ("EC-345", "Computer Vision / Elective", 3.0),
        ("EC-425", "Software Quality Engineering / Elective", 3.0),
        ("MS-254", "Technical and Business Writing", 2.0),
        ("GE-263", "Entrepreneurship", 2.0),
        ("GE-262", "Professional Practices", 2.0),
        ("HQ-007", "Quran Translation - VII", 0.5),
    ],
    8: [
        ("CC-412", "Final Year Project - II", 4.0),
        ("DC-421", "Compiler Construction", 3.0),
        ("UE-272", "Introduction to Marketing", 3.0),
        ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
        ("GE-363", "Civics and Community Engagement", 2.0),
        ("HQ-008", "Quran Translation - VIII", 0.5),
    ],
}
from langchain.tools import tool

def marks_to_grade_points(marks:int)->float:
    '''Convert a given mark to its grade point based on the PUCIT grading scale.
    Use this whenever studnet gives you raw marks like (i got 78 in DB) and you need to convert it to grade points for GPA calculation
    Do not use this when student already gives you grade points like (i got 3.3 in DB) because then you can directly use that for GPA calculation
    '''
    
    if marks<0 or marks >100:
        return "Error: Marks must be between 0 and 100"
    
    if marks>=85:
        return 4.0
    elif marks>=80:
        return 3.7
    elif marks>=75:
        return 3.3
    elif marks>=70:
        return 3.0
    elif marks>=65:
        return 2.7
    elif marks>=61:
        return 2.3
    elif marks>=58:
        return 2.0
    elif marks>=55:
        return 1.7
    elif marks>=50:
        return 1.0
    else:
        return 0.0
 
      
def calculate_semester_gpa(grade_points:list[float],credit_hours:list[float])->float:
    '''Calculate the GPA for one semester using each course's grade point and credit hours.
    Use this when the student wants their semester GPA and you have the
    grade point and credit hours for each course.
    If the student gives marks instead of grade points, first use
    marks_to_grade_points to convert the marks into grade points.
    Do not use this for the overall CGPA of multiple semesters.
    Use calculate_new_cgpa for that.'''
    
    if len(grade_points) != len(credit_hours):
        return "ERROR: Grade points and credit hours lists must be of the same length"
    
    if credit_hours==[] or grade_points==[]:
        return "ERROR: Grade points and credit hours lists cannot be empty"
    
    total_credits=sum(credit_hours)
    
    if total_credits==0:
        return "ERROR:Total Credits cannnot be zero"
    
    total_gp = 0
    for i in range(len(grade_points)):
        total_gp += grade_points[i] * credit_hours[i]
        
    gpa = total_gp / total_credits
    
    return gpa


def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float, semester_gpa: float, semester_credit_hours: float) -> float:
    '''Calculate the new CGPA after completing a semester.
    Use this when the student wants to update their CGPA after a new semester.
    You need the current CGPA, previous total credit hours, current semester GPA,
    and current semester credit hours.
    Do not use this to calculate a single semester's GPA.
    Use calculate_semester_gpa for that.'''
    
    if completed_credit_hours < 0 or semester_credit_hours < 0:
        return "ERROR: Credit hours cannot be negative"
    if semester_credit_hours == 0:
        return "ERROR: Semester credit hours cannot be zero"
    if completed_credit_hours == 0 and current_cgpa != 0:
        return "ERROR: Current CGPA cannot be non-zero if no credit hours have been completed"
    
    total_completed_credits = completed_credit_hours + semester_credit_hours
    
    if total_completed_credits == 0:
        return "ERROR: Total completed credits cannot be zero"
    
    new_cgpa = ((current_cgpa * completed_credit_hours) + (semester_gpa * semester_credit_hours)) / total_completed_credits
    
    return new_cgpa


def required_gpa_for_target(target_cgpa: float, current_cgpa: float, completed_credit_hours: float, remaining_credit_hours: float) ->float:
    '''Calculate the GPA needed in the remaining semesters to reach a target CGPA.
    Use this when the student wants to know what GPA they need in future
    semesters to achieve a specific CGPA.
    You need the target CGPA, current CGPA, completed credit hours,
    and remaining credit hours.
    Do not use this to calculate a semester's GPA or update the current CGPA.
    Use calculate_semester_gpa or calculate_new_cgpa for those tasks..'''
    
    if completed_credit_hours < 0 or remaining_credit_hours < 0:
        return "ERROR: Credit hours cannot be negative"
    if remaining_credit_hours == 0:
        return "ERROR: Remaining credit hours cannot be zero"
    
    total_credits = completed_credit_hours + remaining_credit_hours
    
    required_total_grade_points = target_cgpa * total_credits
    current_total_grade_points = current_cgpa * completed_credit_hours
    
    required_grade_points_for_remaining = required_total_grade_points - current_total_grade_points
    
    required_gpa = required_grade_points_for_remaining / remaining_credit_hours
    
    return required_gpa


def get_semester_courses(semester: int) -> str:
    '''Show the list of courses for a specific semester.
    Use this when the student wants to see the courses in a particular semester.
    You need the semester number from 1 to 8.
    Do not use this for GPA or CGPA calculations.'''
    
    if semester not in COURSES:
        return "ERROR: Invalid sem number  Enter (1-8)"
    
    courses=COURSES[semester]
    lines = []
    for code, name, credits in courses:
        lines.append(f"{code} - {name} ({credits} credits)")

    return "\n".join(lines)
    
    
def get_remaining_credit_hours(current_Semester:int)->float:
    '''Calculate the total credit hours remaining after a given semester.
    Use this when the student wants to know how many credit hours are left to complete after a specific semester.
    You need to provide the current semester number.
    Do not use this for calculating GPA or CGPA.'''
    
    if(current_Semester<1 or current_Semester>8):
        return "ERROR: Invalid sem number  Enter (1-8)"
    total =0
    for sem in range(current_Semester+1,9):
        for code,name,credits in COURSES[sem]:
            total+=credits
            
    return total    
    
    
def save_report(filename: str, content: str) -> str:
    '''Save a report as a text file.
    Use this when the student wants to save a useful result, such as a
    semester GPA, projected CGPA, or target GPA plan.
    Do not use this unless the student asks to save the result.'''

    if not filename.strip():
        return "ERROR: filename cannot be empty"

    if not filename.endswith(".txt"):
        filename += ".txt"

    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"Report saved to {filename}"
    except Exception as e:
        return f"ERROR: could not save file - {e}"
    
  
 
def get_total_credit_hours(semesters: list[int]) -> float:
    """Calculate total credits for a list of semesters.
    Use for one semester or a target CGPA planning window.
    Semester numbers must be between 1 and 8.
    """
    if not semesters or any(s not in COURSES for s in semesters):
        raise ValueError("Provide semester numbers from 1 to 8.")

    if len(semesters) != len(set(semesters)):
        raise ValueError("Do not repeat semester numbers.")

    return sum(
        credits
        for semester in semesters
        for code, name, credits in COURSES[semester]
        if code not in MD
    )  
  
import requests
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()



def send_notification(message: str) -> str:
    """Send a notification to the student's Android phone.
    Use only when the student asks for a notification.
    Provide a short message containing the requested result or link.
    """
    if not message.strip():
        return "Error: Notification message cannot be empty."

    try:
        response = requests.post(
            "https://ntfy.sh/dewo",
            data=message.encode("utf-8"),
            headers={"Title": "Study Assistant"},
            timeout=10,
        )

        response.raise_for_status()

        return "Notification accepted by ntfy for topic dewo."

    except requests.RequestException as error:
        return f"Notification failed: {error}"


web_search_tool = TavilySearch(max_results=3)



def tavily_web_search(query: str) -> dict:
    """Search the web for study resources and relevant information.
    Use when the student requests learning resources or current information.
    Do not use for GPA arithmetic; use the calculation tools instead.
    """
    return web_search_tool.invoke({"query": query})

  

    
    
        