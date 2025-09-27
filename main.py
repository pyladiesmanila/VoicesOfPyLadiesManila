import air

app = air.Air()

@app.get("/")
async def index():
    return air.layouts.mvpcss(
        air.H1("Voices of PyLadies Manila"),
        air.P("Coming soon...")
    )