import re

class TestBaseTemplate:
    def test_base_renders_partials(self, client):
        res = client.get('/')
        assert b'<header>' in res.data
        assert b'<nav>' in res.data
        assert b'<footer>' in res.data
    
    def test_base_renders_main(self, client):
        res = client.get('/')
        assert b'<main>' in res.data
    
    def test_base_contains_script(self, client):
        res = client.get('/')
        assert b'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js' in res.data
    
    def test_base_contains_main_title(self, client):
        res = client.get('/')
        assert b'<title>' in res.data
        assert b'Regressionz' in res.data
    
    def test_base_contains_main_style(self, client):
        res = client.get('/')
        assert b'rel="stylesheet"' in res.data
        assert b'style/main.css' in res.data
    
    def test_base_contains_subheads(self, client):
        res = client.get('/')
        assert b'charset="UTF-8"' in res.data
        assert b'name="viewport"' in res.data
        assert b'name="description"' in res.data
        assert b'property="og:description"' in res.data
        assert b'property="og:title"' in res.data
        assert b'property="og:url"' in res.data
        assert b'property="og:type"' in res.data
        assert b'property="og:image"' in res.data
        assert b'property="twitter:image"' in res.data
        assert b'rel="icon"' in res.data
        assert b'rel="apple-touch-icon"' in res.data

class TestHomeTemplate:
    def test_home_displays_content(self, client):
        res = client.get('/')
        assert b'so much data in our day-to-day lives' in res.data
        assert b'determine multiple regression models' in res.data

    def test_home_displays_signup_plug(self, client):
        res = client.get('/')
        assert b'To join, you just need' in res.data

class TestAboutTemplate:
    def test_about_displays_heading(self, client):
        res = client.get('/about')
        assert b'<h1>About</h1>' in res.data
    
    def test_about_displays_content(self, client):
        res = client.get('/about')
        assert b'provides you with a plethora of data' in res.data
    
    def test_about_displays_subheadings(self, client):
        res = client.get('/about')
        assert b'<h2>What You Get with Each Collection</h2>' in res.data
        assert b'<h2>8 Different Types of Functions</h2>' in res.data
        assert b'<h2>Problems You Can Solve with This API</h2>' in res.data

    def test_about_displays_signup_plug(self, client):
        res = client.get('/about')
        assert b'To join, you just need' in res.data

class TestUsageTemplate:
    def test_usage_displays_heading(self, client):
        res = client.get('/usage')
        assert b'<h1>Usage</h1>' in res.data
    
    def test_usage_displays_content(self, client):
        res = client.get('/usage')
        assert b'guide for how to use the API' in res.data
    
    def test_usage_displays_toc(self, client):
        res = client.get('/usage')
        assert b'<a href="#joining">Sign Up</a>' in res.data
        assert b'<a href="#creating">Create Collection</a>' in res.data
        assert b'<a href="#getting">Get Collection</a>' in res.data
        assert b'<a href="#updating">Update Collection</a>' in res.data
        assert b'<a href="#deleting">Delete Collection</a>' in res.data
        assert b'<a href="#formatting">Format Submissions</a>' in res.data
        assert b'<a href="#interpreting">Interpret Results</a>' in res.data
        assert b'<a href="#example">Example</a>' in res.data
    
    def test_usage_displays_subheadings(self, client):
        res = client.get('/usage')
        assert b'<h2 id="joining">How to Sign Up</h2>' in res.data
        assert b'<h2 id="creating">How to Create a New Collection</h2>' in res.data
        assert b'<h2 id="getting">How to Get an Existing Collection</h2>' in res.data
        assert b'<h2 id="updating">How to Update an Existing Collection</h2>' in res.data
        assert b'<h2 id="deleting">How to Delete an Existing Collection</h2>' in res.data
        assert b'<h2 id="formatting">How to Format Key Fields</h2>' in res.data
        assert b'<h2 id="interpreting">How to Use the Returned Object</h2>' in res.data
        assert b'<h2 id="example">Example</h2>' in res.data
    
    def test_usage_displays_snippets(self, client):
        res = client.get('/usage')
        assert b'https://regressionz.herokuapp.com/api?key=53CR3T491K3Y&source=abc123' in res.data
        assert b'<span class="keys">"independent"</span>: <span class="strings">"month"</span>' in res.data
        assert b'<span class="keys">"sinusoidal_coefficients"</span>' in res.data

class TestMathTemplate:
    def test_math_displays_heading(self, client):
        res = client.get('/math')
        assert b'<h1>Math</h1>' in res.data
    
    def test_math_displays_content(self, client):
        res = client.get('/math')
        assert b'some explanations of mathematical concepts relevant to the output' in res.data
    
    def test_math_displays_toc(self, client):
        res = client.get('/math')
        assert b'<a href="#equations">Equations</a>' in res.data
        assert b'<a href="#correlation">Correlation</a>' in res.data
        assert b'<a href="#points">Points</a>' in res.data
    
    def test_math_displays_subheadings(self, client):
        res = client.get('/math')
        assert b'<h2 id="equations">Equations</h2>' in res.data
        assert b'<h2 id="correlation">Correlation</h2>' in res.data
        assert b'<h2 id="points">Points</h2>' in res.data
    
    def test_math_displays_subsubheadings(self, client):
        res = client.get('/math')
        assert b'<h3>Linear</h3>' in res.data
        assert b'<h3>Quadratic</h3>' in res.data
        assert b'<h3>Cubic</h3>' in res.data
        assert b'<h3>Hyperbolic</h3>' in res.data
        assert b'<h3>Exponential</h3>' in res.data
        assert b'<h3>Logarithmic</h3>' in res.data
        assert b'<h3>Logistic</h3>' in res.data
        assert b'<h3>Sinusoidal</h3>' in res.data
        assert b'<h3>Roots</h3>' in res.data
        assert b'<h3>Maxima</h3>' in res.data
        assert b'<h3>Minima</h3>' in res.data
        assert b'<h3>Inflections</h3>' in res.data
    
    def test_math_displays_graphs(self, client):
        res = client.get('/math')
        assert b'src="/images/linear.png"' in res.data
        assert b'src="/images/quadratic.png"' in res.data
        assert b'src="/images/cubic.png"' in res.data
        assert b'src="/images/hyperbolic.png"' in res.data
        assert b'src="/images/exponential.png"' in res.data
        assert b'src="/images/logarithmic.png"' in res.data
        assert b'src="/images/logistic.png"' in res.data
        assert b'src="/images/sinusoidal.png"' in res.data
        assert b'src="/images/root.png"' in res.data
        assert b'src="/images/maximum.png"' in res.data
        assert b'src="/images/minimum.png"' in res.data
        assert b'src="/images/inflection.png"' in res.data
    
    def test_math_displays_latex(self, client):
        res = client.get('/math')
        latexes = res.data.count(b'$')
        assert latexes == 48

class TestSignupTemplate:
    def test_signup_displays_heading(self, client):
        res = client.get('/signup')
        assert b'<h1>Sign Up</h1>' in res.data
    
    def test_signup_displays_content(self, client):
        res = client.get('/signup')
        assert b'give us your email address' in res.data
    
    def test_signup_displays_form(self, client):
        res = client.get('/signup')
        assert b'form' in res.data
        assert b'<label for="name">Name</label>' in res.data
        assert b'<label for="email">Email</label>' in res.data
        assert b'<input id="submit" name="submit" type="submit" value="Submit">' in res.data