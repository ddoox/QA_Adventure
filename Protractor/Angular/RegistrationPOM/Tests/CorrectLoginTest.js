var loginPage = require('../Pages/LoginPage')
describe('Angular login page', function(){
    it('sholud log in', function(){

        loginPage.get()
        loginPage.setUsername('angular')
        loginPage.setPassword('password')
        loginPage.setuUernameDescription('account description')
        loginPage.login()
        browser.sleep(5000)
    })
})