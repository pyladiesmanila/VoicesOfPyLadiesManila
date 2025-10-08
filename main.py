# Import modified JinjaRenderer
from JinjaRenderer import JinjaRenderer

# Import libraries for Air
import air
from air.requests import Request

app = air.Air()

# Use the modified JinjaRenderer
jinja = JinjaRenderer(directory="templates")


@app.get("/")
async def index(request: Request):
    # Header
    header = air.Header(
        air.Div(
            air.A(
                air.Span("PyLadies", class_="text-[--secondary-purple]"),
                "Manila",
                href="#",
                class_="text-2xl font-extrabold text-gray-800 tracking-tight",
            ),
            air.Nav(
                air.A(
                    "About",
                    href="#about",
                    class_="text-gray-600 hover:text-[--secondary-purple] font-medium transition duration-150",
                ),
                air.A(
                    "Stories",
                    href="#stories",
                    class_="text-gray-600 hover:text-[--secondary-purple] font-medium transition duration-150",
                ),
                air.A(
                    "Contribute",
                    href="#contribute",
                    class_="text-gray-600 hover:text-[--secondary-purple] font-medium transition duration-150",
                ),
                class_="space-x-4",
            ),
            class_="container mx-auto px-6 py-4 flex justify-between items-center",
        ),
        class_="sticky top-0 z-50 bg-white shadow-md",
    )

    # Hero section
    hero_content = {
        "h1": "Voices of PyLadies Manila",
        "h2": "COMING SOON: A web app showcasing the journeys of PyLadies Manila members, from their early days learning programming to their growth as experienced Python developers.",
        "p": "Hear the inspiring stories, challenges, and achievements of Manila's women Python developers.",
    }

    # About the Project stories section
    project_content = {
        "h2": "Our Mission",
        "p1": "Voices of PyLadies Manila is dedicated to documenting women's experiences getting into programming and Python development in Manila. The website serves as a collection of everyone's personal stories and experiences, sharing the unique journeys of women from the time they learned programming, how they built their Python development skills, and what they are currently doing with Python today.",
        "p2": "Each audio clip represents a personal narrative of growth, challenges, and success in the tech field.",
        "h3": "The Collaborative Goal",
        "p3": "This project also exists to give us something fresh to collaborate on together, helping each other build our open-source contribution portfolio and skills. Join us in making this platform a vibrant hub of shared knowledge and achievement!",
    }

    # Featured Stories section
    stories_content = [
        {
            "title": "The Career Switch: From Arts to Code",
            "description": "This story details the transition from a non-technical field into backend Python development, highlighting initial hurdles and finding PyLadies Manila.",
        },
        {
            "title": "Scaling Up: Mastering Django and DevOps",
            "description": "Hear about building complex applications using Python frameworks and navigating the challenges of technical leadership in a fast-paced environment.",
        },
        {
            "title": "First Open Source Contribution",
            "description": "A story focused on a beginner developer's fear of contributing and how working on a community project built confidence and skill.",
        },
    ]

    # Contribution CTA
    contribution_content = {
        "h2": "Contribute and Grow",
        "p": "This project is built by the community, for the community. We welcome developers of all skill levels to help us build our open-source contribution portfolio and skills.",
        "a": "Join the Development Team",
    }

    # Footer
    footer = air.Footer(
        air.Div(
            air.P(
                "Voices of PyLadies Manila - Powered by the Python Community",
                class_="mb-4",
            ),
            air.Div(
                air.A(
                    "PyLadies Manila",
                    href="[LINK_TO_PYLADIES_MANILA_WEBSITE]",
                    class_="text-gray-400 hover:text-[--primary-pink] transition duration-150",
                ),
                air.A(
                    "Privacy",
                    href="[LINK_TO_PRIVACY_POLICY]",
                    class_="text-gray-400 hover:text-[--primary-pink] transition duration-150",
                ),
                air.A(
                    "Terms",
                    href="[LINK_TO_TERMS]",
                    class_="text-gray-400 hover:text-[--primary-pink] transition duration-150",
                ),
                class_="text-sm space-x-4",
            ),
            class_="container mx-auto px-6 text-center",
        ),
        class_="bg-gray-800 text-white py-8",
    )

    return jinja(
        request,
        name="index.html",
        title="Voices of PyLadies Manila | Women in Python Development",
        header=header,
        hero=hero_content,
        project=project_content,
        stories=stories_content,
        contribution=contribution_content,
        footer=footer,
    )
