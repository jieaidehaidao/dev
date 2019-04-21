package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
public class Test {
    @Autowired
    private StringRedisTemplate stringRedisTemplate;
    public void add(String key, String value) {
        add(key, value, null);
    }
    public void add(String key, String value, Long time) {
        stringRedisTemplate.opsForValue().set(key, value);
        if (time != null)
            stringRedisTemplate.expire(key, time, TimeUnit.SECONDS);
    }
    public Object get(String key) {
        return stringRedisTemplate.opsForValue().get(key);
    }
    public void del(String key) {
        stringRedisTemplate.delete(key);
    }

    /**
     * 获取token的有效期
     * @param key
     */
    public long getExpireTime(String key){
        long time = stringRedisTemplate.getExpire(key);
        return time;
    }

    /**
     * 指定时间类型---秒
     * @param key
     * @return
     */
    public long getExpireTimeType(String key){
        long time = stringRedisTemplate.getExpire(key,TimeUnit.SECONDS);
        return time;
    }
}
