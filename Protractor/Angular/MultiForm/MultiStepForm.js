// specs
describe('Angular Form', function() {
    var EC = protractor.ExpectedConditions;
    var name = "login"
    var email = "email@mail.com"
    var console = ['xbox', 'ps']
    var console_select = 0

  
    it('should have a title', function() {
        browser.get('http://www.way2automation.com/angularjs-protractor/multiform/#/form/profile')

        expect(browser.getTitle()).toEqual('Protractor practice website - Multiform')
    });

    it('should complete the form', function() {
        browser.get('http://www.way2automation.com/angularjs-protractor/multiform/#/form/profile')

        element(by.name('name')).sendKeys(name)
        element(by.name('email')).sendKeys(email)
        element(by.css('a[ui-sref="form.interests"]')).click();

        let css_console_select = 'input[value="%s"]'.replace('%s', console[console_select])
        element(by.css(css_console_select)).click();
        element(by.css('a[ui-sref="form.payment"]')).click();

        element(by.css('button[type="submit"]')).click();
        browser.wait(EC.alertIsPresent(), 5000, "Alert is not present")
        browser.switchTo().alert().accept();

        let expected_result = '{"name":"' + name + '","email":"' + email + '","type":"' + console[console_select] + '"}'
        //toMatch because actual result have a lot of whitespaces
        element(by.css('pre[class="ng-binding"]')).getText().then(function(text) {
            return text.trim()
        })

        expect((element(by.css('pre[class="ng-binding"]')).getText())).toMatch(expected_result)
        


    });
  
  
  
    });
  