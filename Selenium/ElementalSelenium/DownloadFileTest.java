import org.openqa.selenium.By;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.testng.annotations.*;
import org.testng.Assert;


import java.io.File;
import java.util.List;
import java.util.UUID;

public class DownloadFileTest {
    private static WebDriver driver;
    File temp_folder;

    @BeforeClass
    public void setUp(){

        temp_folder = new File(UUID.randomUUID().toString());
        temp_folder.mkdir();

        // Set Firefox profile to download files without asking, ask window is from OS - not supported by Selenium
        FirefoxOptions profile = new FirefoxOptions();
        profile.addPreference("browser.download.dir", temp_folder.getAbsolutePath());
        profile.addPreference("browser.download.folderList", 2);
        profile.addPreference("browser.helperApps.neverAsk.saveToDisk",
                "image/jpeg, application/pdf, application/octet-stream");
        profile.addPreference("pdfjs.disabled", true);

        // Hidden windows, faster?
//        profile.addArguments("--headless");

        driver = new FirefoxDriver(profile);
        driver.get("http://the-internet.herokuapp.com/download");
        driver.manage().window().setPosition(new Point(2000,0));
        driver.manage().window().maximize();

    }

    @Test
    public void downloadSingleTest() throws InterruptedException {
        driver.findElement(By.cssSelector("a[href=\"download/Pic.jpg\"]")).click();

        // Wait 5 sec for download
        Thread.sleep(1000);
        // Assert that directory not empty
        File[] listOfFiles = temp_folder.listFiles();
        Assert.assertNotEquals(listOfFiles.length, 0);
        // Assert that files in directory are not empty
        for (File file : listOfFiles) {
            Assert.assertNotEquals(file.length(), 0);
        }
    }

    @Test
    public void downloadAllTest() throws InterruptedException {


        // Get all links in div
        WebElement div_with_links = driver.findElement(By.className("example"));
        List<WebElement> links = div_with_links.findElements(By.cssSelector("a"));
        // Click all links
        // Python way
//        for (WebElement link : links){
//            link.click();
//        }
        int limit = 2;
        for(int i = 0; i < limit; i++){
            links.get(i).click();
            Thread.sleep(500);

        }
        // Assert that directory not empty
        File[] listOfFiles = temp_folder.listFiles();
        Assert.assertNotEquals(listOfFiles.length, 0);
        // Assert that files in directory are not empty
        for (File file : listOfFiles) {
            Assert.assertNotEquals(file.length(), 0);
        }

    }

    @AfterClass
    public void tearDown(){
        driver.quit();

        // Delete Files in folder and folder
        for (File file: temp_folder.listFiles()) {
            file.delete();
        }
        temp_folder.delete();
    }


}
