import pathlib
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

stylesheet = getSampleStyleSheet()
p_style = stylesheet['Normal']
p_style.borderWidth = 1
p_style.borderColor = "#000000"

doc = SimpleDocTemplate(str(files_path.joinpath("fluturas.pdf")))
flowables = []
p1 = Paragraph("SC Excemplu SRL {datetime.now()}", p_style)
p2 = Paragraph("Salariat", p_style)
p3 = Paragraph("Taxe si calcule", p_style)

flowables.append(p1)
flowables.append(p2)
flowables.append(p3)

doc.build(flowables)