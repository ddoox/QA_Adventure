var LoginPage = function() {

    var EC = protractor.ExpectedConditions;
    // default values
    var usernameInput = element(by.id('username'))
    var passwordInput = element(by.id('password'))
    var usernameDescriptionInput = element(by.id('formly_1_input_username_0'))
    var loginButton = element(by.css('button[ng-click="Auth.login()"]'))
    

    // get page
    this.get = function () {
        browser.get('http://www.way2automation.com/angularjs-protractor/registeration/#/login')
    }

    this.setUsername = function (text) {
        usernameInput.sendKeys(text)
    }

    this.setPassword = function (text) {
        passwordInput.sendKeys(text)
    }

    this.setuUernameDescription = function (text) {
        usernameDescriptionInput.sendKeys(text)
    }

    this.login = function (){
        browser.wait(EC.elementToBeClickable(loginButton), 5000)
        loginButton.click()
    }
}
module.exports = new LoginPage()