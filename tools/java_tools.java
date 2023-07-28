// 模拟设备模式
package com.devtools;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import java.util.HashMap;
import java.util.Map;

public class SetDeviceMode{
    final static String PROJECT_PATH = System.getProperty("user.dir");

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", PROJECT_PATH + "/src/main/resources/chromedriver");
        ChromeDriver driver;
        driver = new ChromeDriver();

        DevTools devTools = driver.getDevTools();
        devTools.createSession();
        Map deviceMetrics = new HashMap();
        {{
            put("width", 600);
            put("height", 1000);
            put("mobile", true);
            put("deviceScaleFactor", 50);
        }};
        driver.executeCdpCommand("Emulation.setDeviceMetricsOverride", deviceMetrics);
        driver.get("http://www.google.com");
    }
}




// 模拟地理位置
    @Test
        public void mockLocation(){
            devTools.send(Emulation.setGeolocationOverride(
                Options.of(48.8584),
                Options.of(2.2945),
                Options.of(100)));
            driver.get("https://mycurrentlocation.net/");
            try {
                Thread.sleep(30000);
            }catch(InterruptedException e) {
                e.printStackTrace();
            }
        }






// 模拟网络速度
package com.devtools;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.network.Network;
import org.openqa.selenium.devtools.network.model.ConnctionType;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class SetNetwork{
    final static String PROJECT_PATH = System.getProperty("user.dir");

    public static void main(String[] args){
        System.setProperty("webdriver.chrome.driver", PROJECT_PATH + "/src/main/resources/chromedriver");
        ChromeDriver driver;
        driver = new ChromeDriver();

        DevTools devTools = driver.getDevTools();
        devTools.createSession;
        devTools.send(Network.enable(Optional.empty(), Optional.empty(), Optional.empty()));
        devTools.send(Network.emulateNetworkConditions(
            false,
            20,
            20,
            50,
            Optional.of(ConnctionType.CELLULAR2G)
        ));
        driver.get("https://www.google.com");
    }
}





// 捕获HTTP请求
package com.devtools;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.network.Network;
import java.util.Optional;

public class CaptureNetworkTraffic{
    private static ChromeDriver driver;
    private static  DevTools chromeDriver;

    final static String PROJECT_PATH = System.getProperty("user.dir");

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", PROJECT_PATH + "src/main/resources/chromedriver");
        driver = new ChromeDriver();
        chromeDevTools = new getDevTools();
        chromeDevTools.createSession();

        chromeDevTools.send(Network.enable(Optional.empty(), Optional.empty(), Optional.empty()));
        chromeDevTools.addListener(Network.requestWillBeSent(),
            entry -> {
                System.out.println("Request URL: " + entry.getRequest().getUrl() + "\n" + "Width method:" + entry.getRequest().getMethod() + "\n");
                entry.getRequest().getMethod();
            });
        driver.get("https://www.google.com");
        chromeDevTools.send(Network.disable());
    }
}

// 拦截HTTP响应
    @Test
        public void validateResponse(){
            final RequestId[] requestIds = new RequestId[1];
            devtools.send(Network.enable(Optional.of(100000000), Optional.empty(), Optional.empty()));
            devtools.addListener(Network.reponseReceived(), responseReceived -> {
                if (responseReceived.getResponse().getUrl().contains("api.zoomcar.com")){
                    System.out.println("URL：" + responseReceived.getResponse().getUrl());
                    System.out.println("Status：" + responseReceived.getResponse().getStatus());}
                    System.out.println("Type：" + responseReceived.getType().toJson());
                    responseReceived.getResponse().getHeaders().toJson().forEach(k, v) -> System.out.println(k + ":" + v)));
                    requestIds[0] = responseReceived.getRequestID();
                    System.out.println("Response Body: \n" + devtools.send(Network.getResponseBody(requestIds[0])).getBody() + "\n");
                }
            });
            driver.get("https://www/zoomcar.com/bangalore");
            driver.findElement(By.className("search")).click();
        }





// 访问控制台日志
package com.devtools;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.log.Log;

public class CaptureConsoleLogs{
    private static ChromeDriver driver;
    private static DevTools chromeDevTools;
    final static String PROJECT_PATH = System.getProperty("user.dir");

    public static void main(String[] args){
        System.setProperty("webdriver.chrome.driver", PROJECT_PATH + "/src/main/resources/chromedriver");
        driver = new ChromeDriver();
        chromeDevTools = driver.getDevTools();
        chromeDevTools.createSession();

        chromeDevTools.send(Log.enable());
        chromeDevTools.addListener(Log.entryAdded(),
            logEntry -> {
                System.out.println("log:" + logEntry.getText());
                System.out.println("level:" + logEntry.getLevel());
                }
        );
        driver.get("https://testersplayground.herokuapp.com/console-5d63b2b2-3822-4a01-8197-acd8aa7e1343.php");
    }
}






// 捕获性能指标
package com.devtools;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.performance.Performance;
import org.openqa.selenium.devtools.performance.model.Metric;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class GetMetrics{
    final static String PROJECT_PATH = System.getProperty("user.dir");

    public static void main(String[] args){
        System.setProperty("webdriver.chrome.driver", PROJECT_PATH + "/src/main/resources/chromedriver");
        ChromeDriver driver = new ChromeDriver();
        DevTools devTools = driver.getDevTools();
        devTools.createSession();
        devTools.send(Performance.enable());

        driver.get("https://www.google.com");

        List<Metric> metrics = devTools.send(Performance.getMetrics());
        List<String> metricNames = metrics.stream().map(o -> o.getName()).collect(Collectors.toList());

        devTools.send(Performance.disable());

        List<String> metricsToCheck = Arrays.asList(
            "Timestamp", "Documents", "Frames", "JSEventListeners",
            "LayoutObjects", "MediaKeySessions", "Nodes",
            "Resources", "DomContentLoaded", "NavigationStart");
        metricsToCheck.forEach(metric -> System.out.println(metric + "is: " + metric.get(metricNames.indexOf(metric)).getValue()));
    }
}






// 基本身份验证
package com.devtools;
import org.apache.commons.codec.binary.Base64;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.devtools.DevTools;
import org.openqa.selenium.devtools.network.Network;
import org.openqa.selenium.devtools.network.model.Headers;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class SetAuthHeader{
    private static final String USERNAME = "guest";
    private static final String PASSWORD = "guesr";
    final static String PROJECT_PATH = String.getProperty("user.dir");

    public static void main(String[] args){
        System.setProperty("webdriver.chrome.driver", PROJECT_PATH + '/src/main/resources/chromedriver');
        ChromeDriver driver = new ChromeDriver();

//         create DevTools session and enable Network
            DevTools chromeDevTools = driver.getDevTools();
            chromeDevTools.createSession();
            chromeDevTools.send(Network.enable(Optional.empty(), Optional.empty(), Optional.empty()));

//             open website
            driver.get("https://jigsaw.w3.org/HTTP/");

//             send authorization header
            Map<String, Object> header = new HashMap<>();
            String basicAuth = "Basic " + new String(new Base64().encode(String.format("%s:%s", USERNAME, PASSWORD).getBytes()));
            headers.put("Authorization", basicAuth);
            chromeDevTools.send(Network.setExtraHTTPHeaders(new Headers(headers)));

//             click authentication test - this narmally invokes a browser papup if unauthenticated
            driver.findElement(By.linkText("Basic Authentication test")).click();

            String loginSuccessMsg = driver.findElement(By.tagName("html")).getText();
            if (loginSuccessMsg.contains("Your browser made it!")){
                System.out.println("Login successful");
            }else{
                System.out.println("Login failed");
            }
            driver.quit();
    }
}