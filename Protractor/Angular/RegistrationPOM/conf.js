exports.config = {
      // The address of a running selenium server.
    seleniumAddress: 'http://localhost:4444/wd/hub',
    specs: ['Tests/CorrectLoginTest.js'],
    capabilities: {
        browserName: 'firefox',
        firefoxPath: 'C:/Program Files/Mozilla Firefox/firefox.exe'
      },
  };