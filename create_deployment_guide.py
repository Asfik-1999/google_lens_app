from fpdf import FPDF  # Confirm this is from fpdf2, which supports UTF-8

class DeploymentGuide(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_font('Helvetica', 'B', 24)
        self.cell(0, 20, 'OCR Web Application Deployment Guide', 0, 1, 'C')
        self.ln(10)

    def add_section(self, title, content):
        self.set_font('Helvetica', 'B', 16)
        self.cell(0, 10, title.encode('latin-1', 'ignore').decode('latin-1'), 0, 1, 'L')
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 10, content.encode('latin-1', 'ignore').decode('latin-1'))
        self.ln(5)

    def add_code(self, code):
        self.set_font('Courier', '', 10)
        self.set_fill_color(240, 240, 240)
        self.multi_cell(0, 8, code.encode('latin-1', 'ignore').decode('latin-1'), 1, 'L', True)
        self.ln(5)

def create_deployment_guide():
    pdf = DeploymentGuide()
    
    # Section 1: Prerequisites
    pdf.add_section('1. Prerequisites', 
        'Before starting, ensure you have:\n'
        '- Python 3.8 or higher\n'
        '- Git installed\n'
        '- Tesseract OCR installed\n'
        '- A GitHub account\n'
        '- Basic command line knowledge')

    # Section 2: Project Setup
    pdf.add_section('2. Project Setup', 
        'First, organize your project files in the following structure:')
    
    pdf.add_code(
        'your_project/\n'
        '├── app.py\n'
        '├── static/\n'
        '│   └── style.css\n'
        '├── templates/\n'
        '│   └── index.html\n'
        '├── requirements.txt\n'
        '├── Procfile\n'
        '└── runtime.txt')

    # Section 3: Deployment Options
    pdf.add_section('3. Deployment Options',
        'You have several options for hosting your application:')
    
    # PythonAnywhere
    pdf.add_section('Option A: PythonAnywhere (Recommended for Beginners)',
        '1. Sign up at www.pythonanywhere.com\n'
        '2. Create a new web app\n'
        '3. Choose Python 3.9 and Flask\n'
        '4. Upload your files\n'
        '5. Install requirements\n'
        '6. Configure WSGI file')
    
    pdf.add_code(
        '# In PythonAnywhere console:\n'
        'pip install -r requirements.txt\n'
        'pip install pytesseract\n'
        'pip install pdf2image')

    # Heroku
    pdf.add_section('Option B: Heroku',
        '1. Create Heroku account\n'
        '2. Install Heroku CLI\n'
        '3. Login to Heroku\n'
        '4. Create new app\n'
        '5. Deploy application')
    
    pdf.add_code(
        'heroku login\n'
        'heroku create your-app-name\n'
        'git add .\n'
        'git commit -m "Initial deployment"\n'
        'git push heroku main')

    # Security Considerations
    pdf.add_section('4. Security Considerations',
        '- Set up environment variables\n'
        '- Configure SSL certificate\n'
        '- Implement rate limiting\n'
        '- Add file validation\n'
        '- Set up proper error handling')

    # Monitoring
    pdf.add_section('5. Monitoring',
        '- Set up application logging\n'
        '- Configure error notifications\n'
        '- Monitor server resources\n'
        '- Set up backup system')

    # Save the PDF
    pdf.output('deployment_guide.pdf')

if __name__ == '__main__':
    create_deployment_guide()
