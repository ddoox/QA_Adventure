import org.openqa.selenium.By;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.*;

import java.io.File;

@Test
public class UploadFileTest {
    private static WebDriver driver;

    @BeforeClass
    public void setUp() throws Exception {
        System.setProperty("webdriver.gecko.driver","Drivers/geckodriver.exe");
        driver = new FirefoxDriver();
        driver.manage().window().setPosition(new Point(2000,0));
        driver.manage().window().maximize();
        driver.get("http://the-internet.herokuapp.com/upload");
    }

    @Test
    public void uploadElementExists() throws Exception{
        driver.findElement(By.id("file-upload"));
    }

    @Test
    public void submitElementExists() throws Exception{
        driver.findElement(By.xpath("//*[@id=\"file-submit\"]\n"));
    }

    @Test
    public void uploadFile() throws Exception{
        File file = new File("Selenium/README.md");
        String path = file.getAbsolutePath();
        driver.findElement(By.id("file-upload")).sendKeys(path);
        driver.findElement(By.xpath("//*[@id=\"file-submit\"]\n")).click();
        String actual = driver.findElement(By.id("uploaded-files")).getText();
        Assert.assertEquals(actual,file.getName());
    }

    @AfterClass
    public void tearDown() throws Exception{
        driver.quit();
    }


}
