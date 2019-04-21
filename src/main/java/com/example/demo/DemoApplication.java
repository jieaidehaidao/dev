package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@EnableCaching
@SpringBootApplication
public class DemoApplication {

	@Autowired
	Test test;

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@ResponseBody
	@RequestMapping("/get")
	public Object hello(String key){
		return test.get(key);
	}

	@ResponseBody
	@RequestMapping("/del")
	public Object world(String key){
		test.del(key);
		return true;
	}

	@ResponseBody
	@RequestMapping("/add")
	public Object add(String key,String value){
		test.add(key,value);
		return true;
	}

    @ResponseBody
    @RequestMapping("/ttl")
    public Object ttl(String key){
        return test.getExpireTimeType(key);
    }

}
