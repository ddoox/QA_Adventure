exports.config = {
    seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['MultiStepForm.js'],
    capabilities: {
        browserName: 'firefox',
        firefoxPath: 'C:/Program Files/Mozilla Firefox/firefox.exe'
      },
  };