// specs
describe('Protractor Demo App', function() {

    it('should have a title', function() {
      browser.waitForAngularEnabled(false) // Don't wait for Angular to load
      browser.get('http://the-internet.herokuapp.com/');
  
      expect(browser.getTitle()).toEqual('The Internet');
    });

    it('should be failure', function() {
        browser.waitForAngularEnabled(false) // Don't wait for Angular to load
        browser.get('http://the-internet.herokuapp.com/');
    
        expect(browser.getTitle()).toEqual('The Irnternet');
      });

    it('should display message after log in', function() {
        browser.waitForAngularEnabled(false) // Don't wait for Angular to load
        browser.get('http://the-internet.herokuapp.com/login');

        element(by.css('input[type="text"]')).sendKeys('tomsmith')
        element(by.id('password')).sendKeys('SuperSecretPassword!')
        element(by.className('.fa.fa-2x.fa-sign-in')).parentElementArrayFinder.click()

        expect(element(by.className('.flash.success')).isPresent())
        browser.driver.sleep(1000)
        });

  });
