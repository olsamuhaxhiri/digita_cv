import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | "
PAGE_ICON = ":wave:"
NAME = "Olsa Muhaxhiri"
DESCRIPTION = """
Data Scientist  in making and data-driven decision-making.
"""

EMAIL = "olsamuhaxhiri@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/olsamuhaxhiri"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "/workspaces/digita_cv/assets/OlsaMuhaxhiriResume.pdf"
profile_pic_file = "assets/Screenshot 2026-06-13 210430.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Experience in full-stack web development using ASP.NET Core, React.js, and Next.js.
- ✔️ Strong knowledge of C#, Python, SQL, REST APIs, and database management.
- ✔️ Skilled in designing scalable applications and implementing software engineering best practices.
- ✔️ Familiar with software testing, debugging, quality assurance, and system integration.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: C#, Python, JavaScript, SQL
- 🌐 Web Development: ASP.NET Core, React.js, Next.js
- 🗄️ Databases: SQL Server, PostgreSQL, MySQL
- 🔗 APIs: RESTful APIs, Swagger, Postman
- 🧪 Testing & QA: Manual Testing, Bug Reporting, API Testing
- 🛠️ Tools: Git, GitHub, Visual Studio, VS Code
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Projects & Experience")
    st.write("---")

    # --- PROJECT 1
    st.write("🚧", "**Full-Stack Developer | Academic & Personal Projects**")
    st.write("2024 - Present")
    st.write(
        """
- ► Developed full-stack web applications using ASP.NET Core and React.js.
- ► Designed and implemented RESTful APIs following clean architecture principles.
- ► Managed relational databases and optimized data access using Entity Framework.
- ► Applied design patterns and software engineering best practices.
"""
    )

    # --- PROJECT 2
    st.write("\n")
    st.write("🚧", "**Software Development Projects | University**")
    st.write("2023 - Present")
    st.write(
        """
- ► Built CRUD applications with authentication and authorization features.
- ► Developed backend services and integrated frontend interfaces.
- ► Implemented Repository Pattern and Hexagonal Architecture in academic projects.
- ► Worked with API integration and database design.
"""
    )

    # --- PROJECT 3
    st.write("\n")
    st.write("🚧", "**Quality Assurance & Testing Experience**")
    st.write("2025 - Present")
    st.write(
        """
- ► Performed manual testing of web applications.
- ► Created and executed test cases and reported defects.
- ► Tested REST APIs using Postman and Swagger.
- ► Verified functionality, usability, and responsiveness across devices.
"""
    )

elif page == "About":
    st.title("About Me")

    st.write("""
I am a Computer Science student passionate about software development,
web technologies, and building innovative digital solutions.

With experience in C#, ASP.NET Core, React.js, Next.js, Python, SQL,
and API development, I enjoy designing scalable applications, solving
complex technical problems, and creating user-focused systems.

My background includes developing web applications, implementing backend
services, working with databases, and applying software engineering
principles such as design patterns and modern architectures.

I am continuously expanding my skills in software development, quality
assurance, data analytics, and emerging technologies, with a strong
commitment to learning and delivering high-quality results.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")
