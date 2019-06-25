# 一、负载均衡和HTTP缓存

## 1.1 高性能的负载均衡

如今的互联网产品的用户体验依赖与产品的可用时间和服务性能。为实现这些目标，多个相同服务被部署在物理设备上构建称`服务集群`，并`使用负载均衡实现请求分发`；随着负载的增加，新的服务会被部署到到集群中；这种技术称之为`水平扩展`。由于其灵活性，基于软件的可扩展技术越来越受到青睐。而无论是仅有两台服务器的高可用技术方案，还是成千上万台服务器的高可用集群，它们的可用性都需要灵活的负载均衡解决方案才能得以保障。NGINX提供了多种协议的负载均衡解决方案如：HTTP、TCP 和 UDP 负载均衡，其中UDP 负载均衡将在第 9 章讲解。

本章将讨论 HTTP 和 TCP 负载均衡技术。还将学习`负载均衡算法`如：`轮询`，`最少连接数`，`最短响应时间`，`IP 哈希`和`普通哈希`。这些负载均衡算法有助于您在项目中选择行之有效的请求分配策略。此外，还将讲解如何将更多的请求分配到那些服务器性能更好的机器上。

### 1.1.1 HTTP 负载均衡

- 问题：

将用户请求分发到 2 台以上 HTTP 服务器。

- 解决方案：

使用 `NGINX` 的 `HTTP` 模块，将请求分发到有 `upstream` 块级指令代理的 `HTTP` 服务器集群，实现负载均衡：

```nginx
upstream backend {
    server 10.10.12.45:80 weight=1;
    server app.example.com:80 weight=2;
}
server {
    location / {
        proxy_pass http://backend;
    }
}
```

配置中启用了两台默认 `80 端口` `HTTP` 服务器 构成服务器集群。`weight` 参数表示每三个请求将有 2 个请求分发到 app.example.com:80 服务器，它的默认值为 1。

- 结论：

HTTP 模块的 `upstream` 用于设置被代理的 HTTP 服务器实现负载均衡。

模块内定义一个目标服务器连接池，它可以是 `UNIX 套接字`、`IP 地址`、`DNS 记录`或它们的混合使用配置；此外 upstream 还可以通过 `weight` 参数配置，如何分发请求到应用服务器。

所有 HTTP 服务器在 upstream 块级指令中由 `server` 指令配置完成。

server指令接收` UNIX 套接字`、`IP 地址`或 `FQDN`(Fully Qualified Domain Name: 全限定域名) 及一些可选参数。可选参数能够精细化控制请求分发。它们包括用于负载均衡算法的 weight 参数；判断目标服务器是否可用，及如何判断服务器可用性的 `max_fails` 指令和 `fail_timeout` 指令。NGINX Plus 版本提供了许多其他方便的参数，比如服务器的连接限制、高级DNS解析控制，以及在服务器启动后缓慢地连接到服务器的能力。

### 1.1.2 TCP 负载均衡

- 问题:

将请求分发到 2 台以上 TCP 服务器。

- 解决方案：

在 NGINX 的 `stream` 模块内使用 `upstream` 块级指令实现多台 `TCP` 服务器负载：

```nginx
stream {
    upstream mysql_read {
        server read1.example.com:3306 weight=5;
        server read2.example.com:3306;
        server 10.10.12.34:3306 backup;
    }
    server {
        listen 3306;
        proxy_pass mysql_read;
    }
}
```

例中的 `server` 块级指令指定 `NGINX` 监听 `3306` 端口的多台 `MySQL` 数据库实现负载均衡，其中 `10.10.12.34:3306` 作为备用数据库服务器当负载请求分发失败时会被启用。

- 结论：

TCP 负载均衡在 stream 模块中配置实现。stream 模块类似于 http 模块。

配置时需要在 server 块中使用 listen 指令配置待监听端口或 IP 加端口。接着，需要明确配置目标服务，目标服务可以使代理服务或 upstream 指令所配置的连接池。 TCP 负载均衡实现中的 upstream 指令配置和 HTTP 负载均衡实现中的 upstream 指令配置相似。TCP 服务器在 server 指令中配置，格式同样为 UNIX 套接字、IP地址或 FQDN(Fully Qualified Domain Name:全限定域名)；用于精细化控制的 weight 权重参数、最大连接数、DNS 解析器、判断服务是否可用和启用为备选服务的 backup 参数一样能在 TCP 负载均衡中使用。

### 1.1.3 负载均衡算法

- 问题:

对于负载压力不均匀的应用服务器或服务器连接池，`轮询(round-robin)`负载均衡算法无法满足业务需求。

- 解决方案：

使用 NGINX 提供的其它负载均衡算法，如：`最少连接数(least connections)`、`最短响应时间(leaest time)`、`通用散列算法(generic hash)`或 `IP 散列算法(IP hash)`：

```nginx
upstream backend {
    least_conn;
    server backend.example.com;
    server backend1.example.com;
}
```

上面的 `least_conn` 指令为 upstream 所负载的后端服务，指定采用`最少连接数负载均衡算法`实现负载均衡。

所有的负载均衡算法指令，除了通用算列指令外，都和上面示例一样是一个普通指令，需要独占一行配置。通用散列指令，接收一个参数，也可以使一系列变量值的拼接结果，来构建散列值。

- 结论：

在负载均衡中，并非所有的请求和数据包请求都具有相同的权重。有鉴于此，如上例所示的轮询或带有权重的轮询负载均衡算法，可能并不能满足我们的应用或负载需求。NGINX 提供了一系列的负载均衡算法，以满足不同的运用场景。所有提供的负载均衡算法都可以针对业务场景随意选择和配置，并且都可以应用于 upstream 块级指令中的 HTTP、TCP 和 UDP 负载均衡服务器连接池。

- A. 轮询负载均衡算法(Round robin)

NGINX 服务器默认的负载均衡算法，该算法将请求分发到 upstream 指令块中配置的应用服务器列表中的任意一个服务器。可以通过应用服务器的负载能力，为应用服务器指定不同的分发权重(weight)。权重的值设置的越大，将被分发更多的请求访问。权重算法的核心技术是，依据访问权重求均值进行概率统计。轮询作为默认的负载均衡算法，将在没有指定明确的负载均衡指令的情况下启用。

- B. 最少连接数负载均衡算法(Least connections)

NGINX 服务器提供的另一个负载均衡算法。它会将访问请求分发到upstream 所代理的应用服务器中，当前打开连接数最少的应用服务器实现负载均衡。最少连接数负载均衡，提供类似轮询的权重选项，来决定给性能更好的应用服务器分配更多的访问请求。该指令的指令名称是`least_conn`。

- C. 最短响应时间负载均衡算法(least time)

该算法仅在 NGINX PLUS 版本中提供，和最少连接数算法类似，它将请求分发给平均响应时间更短的应用服务器。它是负载均衡算法最复杂的算法之一，能够适用于需要高性能的 Web 服务器负载均衡的业务场景。该算法是对最少连接数负载均衡算法的优化实现，因为最少的访问连接并非意味着更快的响应。该指令的配置名称是 `least_time`。

- D. 通用散列负载均衡算法(Generic hash)

服务器管理员依据请求或运行时提供的文本、变量或文本和变量的组合来生成散列值。通过生成的散列值决定使用哪一台被代理的应用服务器，并将请求分发给它。在需要对访问请求进行负载可控，或将访问请求负载到已经有数据缓存的应用服务器的业务场景下，该算法会非常有用。需要注意的是，在 upstream 中有应用服务器被加入或删除时，会重新计算散列进行分发，因而，该指令提供了一个可选的参数选项来保持散列一致性，减少因应用服务器变更带来的负载压力。该指令的配置名称是 `hash`。

- E. IP 散列负载均衡算法(IP hash)

该算法仅支持 HTTP 协议，它通过计算客户端的 IP 地址来生成散列值。不同于采用请求变量的通用散列算法，IP 散列算法通过计算 IPv4 的前三个八进制位或整个 IPv6 地址来生成散列值。这对需要存储使用会话，而又没有使用共享内存存储会话的应用服务来说，能够保证同一个客户端请求，在应用服务可用的情况下，永远被负载到同一台应用服务器上。该指令同样提供了权重参数选项。该指令的配置名称是 `ip_hash`。

## 1.3 服务器健康监控

访问应用时，可能由于网络连接失败，Web 服务器宕机或应用程序异常等原因导致应用程序无法访问。这时，代理或负载均衡器需要提供能够智能检测被代理或被负载的 Web 服务是否无法访问的能力，来确保不会请求分发到这些失效的服务器。同时，客户端会收到连接超时的响应，结束请求等待状态。

通过代理服务器向被代理服务器发送健康检测请求，来判断被代理服务器是否失效，是一种减轻被代理服务器压力的有效方法。NGINX 服务器提供两种不同的健康检测方案：被动检测和主动检测，开源版的 NGINX 提供被动检测功能， NGINX PLUS 提供主动检测功能。主动检测的实现原理是，NGINX 代理服务向被代理服务器定时的发送连接请求，如果被代理服务器正常响应，则说明被代理服务器正常运行。被动检测的实现原理是：NGINX 服务器通过检测客户端发送的请求及被代理(被负载均衡)服务器的响应结果进行判断被代理服务器是否失效。被动检测方案，可以有效降低被代理服务器的负载压力；主动检测则能够在客户端发送请求之前，就能够剔除掉失效服务器。

### 1.3.1 健康监控内容

- 问题:

你想对服务器进行有效检测，但不止如何去检测服务器健康状况。

- 解决方案：

使用一个简单粗暴的检测方案实现应用健康检测。如，负载均衡器通过获取被负载服务器的响应状态码是否为 200 判断应用服务器进程是否正常。

- 结论：

实际项目中，对被负载的提供核心功能的应用服务器进行健康检测非常重要。仅仅通过一种健康检测方案，确保核心服务是否可用，通常并不完全可靠。健康检测应该通过网络直接检测被负载的应用服务器和应用本身是否运行正常，来确保服务可用，这比仅使用负载均衡器来检测服务是否可用要可靠。一般，可以选择一个功能来进行健康检测，来确保整个服务是否可用。比如，确认数据库连接是否正常或应用是否能够正常获取它的资源。任何一个服务失效，都可能引发蝴蝶效应导致整个服务不可用。

### 1.3.3 TCP 服务器监控检测

- 问题:

需要检测 TCP 服务器是否正常并从代理池中移除失效服务器。

- 解决方案：

在 server 块级指令中 使用 health_check 简单指令，对被代理服务器进行健康检测:

```nginx
stream {
    server {
        listen 3306;
        proxy_pass read_backend;
        health_check interval=10 passes=2 fails=3;
    }
}
```

上面的配置会对代理池中的服务器进行主动监测。如果被代理服务器未能正常响应 NGINX 服务器的 3 个以上 TCP 连接请求，则被认为是失效的服务。之后，NGINX 服务器会每隔 10 秒进行一次健康检测。

- 结论：

在 NGINX PLUS 版本中同时提供被动检测和主动检测功能。被动检测是通过加之于客户端与被代理服务器的请求响应检测实现的。如果一个请求超时或者连接失败，被动检测则认为该被代理服务器失效。主动检测则是通过明确的 NGINX 指令配置来检测服务器是否失效。主动检测途径可以是一个测试的连接，也可以是一个预期的响应。

[>> TCP服务器监控检测官方文档](https://docs.nginx.com/nginx/admin-guide/load-balancer/tcp-health-check/)

### 1.3.4 HTTP 服务器监控检测

- 问题:

需要主动检测 HTTP 服务器健康状态

- 解决方案：

在 location 块级指令中使用 health_check 指令检测：

```nginx
http {
    server {
        ...
        location / {
            proxy_pass http://backend;
            health_check interval=2s
                         fails=2
                         passes=5
                         uri=/
                         match=welcome;
        }
    }

    # status is 200, content type is "text/html",
    # and body contains "Welcome to nginx!"
    match welcome {
        status 200;
        header Content-Type = text/html;
        body ~ "Welcome to nginx!";
    }
}
```

上例，通过向被代理服务器每隔 2 秒，发送一个到 '/' URI 的请求来检测被代理服务器是否失效。被代理服务器连续接收 5 个请求，如果其中有 2 个连续请求响应失败，将被视作服务器失效。被代理服务器的健康响应格式在 match 块级指令中配置，规定响应状态码为 200, 响应Content-Type类型为'text/html',响应 body 为 "Welcome to nginx!" 字符串的响应为有效服务器。

- 结论：

在 NGINX PLUS 版本中，除了通过响应状态码来判断被代理服务器是否有效。还能够通过其它的一些响应指标来判断是否有效。如：主动检测的时间间隔(频率)，主动请求的 URI 地址，健康检测的请求次数及失败次数和预期响应结果等。在 health_check 指令中的 match 参数指向 match 块级指令配置，match 块级指令配置定义了标准的响应，包括 status、header 和 body 指令，他们都有各自的检测标准。

[>> HTTP服务器监控检测官方文档](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-health-check/)

## 1.5 大规模可伸缩缓存配置

通过对请求的响应结果进行缓存，能够为后续相同请求提供加速服务。对相同请求响应内容进行内容缓存(Content Caching)，相比每次请求都重新计算和查询被代理服务器，能有效降低被代理服务器负载。内容缓存能提升服务性能，降低服务器负载压力，同时意味着能够使用更少的资源提供更快的服务。可伸缩的缓存服务从架构层面来讲，能够显著提升用户体验，因为响应内容经过更少的转发就能够发送给用户，同时能提升服务器性能。

### 1.5.1 缓存区域配置（Caching Zones）

- 问题:

需要定义响应内容的缓存路径及缓存操作

- 解决方案：

使用 proxy_cache_path 指令为待缓存定义内容缓存区域的共享内存及缓存路径：

```nginx
proxy_cache_path /var/nginx/cache
            keys\_zone=CACHE:60m

            levels=1:2

            inactive=3h

            max\_size=20g;
proxy_cache CACHE;
```

上面的配置中在 `proxy_cache_path` 指令中为响应在文件系统中定义了缓存的存储目录 /var/nginx/cache，并使用 `keys_zone` 参数创建名为 CACHE 的拥有 60 M 的缓存内存空间；同时通过 `levels` 参数定义目录解构级别，通过 `inactive` 参数指明如果相同请求的缓存在 3 小时内未被再次访问则被释放，并使用 `max_size` 定义了缓存最大可用存储空间为 20 G。

- 结论：

要使用 NGINX 内容缓存，需要在配置中定义缓存目录及缓存区域(zone)。通过 proxy_cache_path 指令创建 NGINX 内容缓存，定义用于缓存信息的路径和用于存储缓存的元数据(metadata)和运行时键名(active keys)的共享内存。其它的可选参数，还提供缓存如何维护和访问的控制，levels 参数定义如何创建文件结构，定义子目录的文件名长度，语法是以冒号分隔的值，支持最大 3 级。

NGINX 的所有缓存依赖于最终被计算成散列的 cache key，接着将结果以 cache key 作为文件名，依据缓存级别创建缓存目录。

inactive 参数用于控制最后一次使用缓存选项的时间，超过这个时间的缓存会被释放。缓存的大小则可以通过 max_size 参数进行配置。还有部分参数作用于缓存加载进程中，功能是将 cache keys 从磁盘文件加载仅共享内存里。

### 1.5.2 配置缓存哈希键名

- 问题:

自定义如何缓存和查找缓存内容

- 解决方案：

通过一条单独的 `proxy_cache_key` 指令，以变量名的形式定义缓存命中和丢弃的规则。

```nginx
proxy_cache_key "$host$request_uri $cookie_user";
```

上例指令依据请求域名、请求 URI 和用户 cookie 作为缓存键名，来构建 NGINX 的缓存页面。这样，就可以对动态页面进行缓存，而无需对每个用户都进行缓存内容的生成处理。

- 结论：

proxy_cache_key 默认设置是 "$scheme$proxy_host $request_uri"。默认设置适用于多数的使用场景。配置之中包括 scheme、HTTP 或 HTTPS、代理域名(proxy_host)、请求的 URI 等变量。总之，它们能够正确处理 NGINX 代理请求。

您可能会发现，对于每个应用程序，有许多其他的因素可以定义一个惟一的请求，比如请求参数、头文件、会话标识符等等，您需要创建自己的散列键。或许你已经发现，对一个应用，还有其它的数据能够确定一个唯一的请求，比如请求参数、请求头(headers)、会话标识(session identifiers) 等等，这些都可以用于构建自己的散列键名。在构建时应基于应用程序的理解，创建选择一个好的散列键名，这一点非常重要。比较简单的是为静态内容创建缓存键名，通常，可以直接使用域名(hostname)和请求 URI 就可以了。而类似于仪表盘这类的，具有动态内容的页面，则需要充分了解用户和应用之间的交互、以及用户体验之间的差异，来构建缓存键名。如从安全的角度触发，你可能不希望缓存将一个用户的缓存数据展示给另外的用户。proxy_cache_key 令配置了用于缓存生成哈希值字符，此条指令可以在 HTTP、server、location 块级指令上下文中定义，实现对请求如何缓存的灵活控制。

### 1.5.3 跳过被缓存内容

- 问题:

将一些内容不进行缓存

- 解决方案：

将 `proxy_cache_passby` 指令，设置称非空值或非 0。一种途径是，在 location 块级指令中设置一个值等于 1 的 proxy_cache_passby 指令：

```nginx
proxy_cache_bypass $http_cache_bypass;
```

配置告知 NGINX 服务器，如果一个 HTTP cache_passby 请求头的值设置为非 0(或非空)，则不对该请求进行缓存处理。

- 结论：

挺多应用场景下都不应对请求进行缓存处理，对此，NGINX 提供 proxy_cache_passby指令来应对这些场景。通过将指令值设置为非空或非零，匹配的请求 URI 会直接发送给被代理服务器，而不是从缓存中获取。如何使用该指令，需要结合客户端和应用的实际使用。它既可以配制成如同一个请求变量一样简单，也可以配置成复杂的映射指令块。但最终目的都是绕过缓存。其中，一个重要的应用场景就是排除故障和调试应用。如果在研发过程中一直使用缓存，或对特定用户进行缓存，缓存会影响问题的复现。提供对指定cookie、请求头(headers)或请求参数等的缓存绕过能力，则是一个必要的功能。此外，NGINX 服务器还能够在 location 块指令中将 proxy_cache 指令设置为 off，完全禁用缓存。

### 1.5.4 缓存性能

- 问题:

需要在客户端提升服务性能

- 解决方案：

使用客户端缓存控制消息头：

```nginx
location ~* .(css|js)$ {
    expires 1y;

    add\_header Cache-Control "public";
}
```

该 location 块指令设置成功后，客户端可以对 CSS 和 JS 文件进行缓存。expires 指令将所有缓存的有效期设置为 1 年。add_header 指令将 HTTP 消息头 Cache-Control 设置成 public 并加入响应中，表示所有的缓存服务器都可以缓存资源。如果将它的值设置为 private，则表示仅允许客户端对资源进行缓存。

- 结论：

缓存的性能和许多因素有关，其中磁盘读写速度是影响缓存性能的重要原因之一。在 NGINX 配置指令中，还有很多能够提升性能的指令。像上例中配置的，通过设置 Cache-Control 响应消息头，客户端会直接从本地读取缓存，而不会将请求发送给服务器来提升性能。

## 1.9 UDP 负载均衡

用户数据报协议(UDP) 在多种场景下运用，如 DNS、NTP 服务、IP语音(Voice over IP)服务。NGINX 可以在 upstream 块级指令中使用所有的负载均衡算法实现 UDP 的负载均衡，本章将学习 UDP 负载均衡相关配置。

### 1.9.1 Stream 指令上下文

- 问题:

需要在多台 UDP 服务器间实现负载均衡

- 解决方案：

NGINX stream 模块实现 UDP 服务器的负载均衡，作为 UDP 服务器的代理的 upstream 块级指令被定义称使用 UDP 协议:

```nginx
stream {
    upstream ntp {

        server ntp1.example.com:123 weight=2;

        server ntp2.example.com:123;

    }

    server {

        listen 123 udp;

        proxy\_pass ntp;

    }
}
```

示例中，对 2 台使用 UDP 协议的 NTP 服务器进行负载均衡代理。实现 UDP 协议的负载均衡，简单到仅需在 server 指令块中的 listen 指令加上一个 udp 参数就可以了。

- 结论：

或许有人会问 “既然有多条 A 记录或 SRV 记录的 DNS 域名解析，为什么我还需要使用 NGINX 的负载均衡功能呢？” 

我们的理由是，NGINX 不仅提供了多种负载均衡算法，而且还能对 DNS 服务器本身进行负载均衡处理。UDP 协议构建了 DNS 解析、NTP 服务器、IP 语音服务等大量基础服务。UDP 负载均衡在某些场景下运用不是特别广泛，但在整个网络世界则并非如此。

UDP 负载均衡同 TCP 负载均衡一样集成在 stream 模块内，并且它们的使用方法也几乎一样。二者的主要区别是，在 listen 指令中定义用于 UDP 协议的套接字及 udp 参数。此外，还有一些仅用于 UDP 协议的指令，像 proxy_response 指令，proxy_response 指令告知 NGINX 服务器从被代理服务器接收多少预期响应，默认是无限制的，直到达到 proxy_timeout 设定值。

### 1.9.3 UDP 服务器健康检测

- 问题:

检测 upstream 指令中的 UDP 服务器是否健康。

- 解决方案：

对 UDP 负载均衡配置进行健康检测，确保只对正常运行的 UDP 服务器发送数据报文：

```nginx
upstream ntp {
    server ntp1.example.com:123 max\_fails=3 fail\_timeout=3s;
    server ntp2.example.com:123 max\_fails=3 fail\_timeout=3s;
}
```

配置采用被动检测功能，将 max_fails 指令设置为 3 次，fail_timeout 设置为 3 秒。

- 结论：

无论何种负载均衡，无论从用户体验角度，还是商业角度，健康检测都至关重要。NGINX 同样提供 UDP 负载均衡主动和被动检测方案。被动检测会监测连接失败及超时请求作为失效服务判断。主动检测会主动发送数据包值指定端口，通过配置的预期响应判断服务是否有效。

# 二、服务器安全与可访问性

## 2.11 可访问性控制

本书的第二部分将讲解 NGINX 和 NGINX PLUS 版本的安全特性。通过第二部分相关知识，您将掌握如何配置 NGINX 服务器才能有效控制服务器资源不被应用程序滥用。学习安全配置，如 NGINX 服务器如何使用对请求数据加密和基本的HTTP 认证。更高级的安全配置，像 NGINX 服务器如何使用第三方认证系统进行身份认证，如何使用 JSON 令牌校验和单点登录功能等。此外，您还将学习NGINX 和 NGINX PLUS 版本更多惊艳的特性，如访问次数控制、使用 NGINXPLUS 版本的 ModSecurity 模块开启防火墙功能等等。对于一些即插即用(plug-and-pay)模块，仅能通过 NGINX PLUS 版本订阅获取，然而，这并不意味着免费版的 NGINX 服务器不能使用。

### 2.11.1 基于IP地址访问配置

- 问题:

需要基于客户端的 IP 地址实现访问控制功能

- 解决方案：

使用 HTTP 的 access 模块，实现对受保护资源的访问控制：

```nginx
location /admin/ {
    deny 10.0.0.1;
    allow 10.0.0.0/20;
    allow 2001:0db8::/32;
    deny all;
}
```

给定的 location 块级指令中配置了允许除 10.0.0.1 外的所有 10.0.0.0/20 IPv4 地址访问，同时允许 2001:0db8::/32 及其子网的 IPv6 地址访问，其它 IP 地址 的访问将会收到 HTTP 状态为 403 的响应。allow 和 deny 指令可在 HTTP、server、location 上下文中使用。控制规则依据配置的顺序进行查找，直到匹配到控制规则。

- 结论：

需要控制访问的资源需要实现分层控制。NGINX 服务器提供对资源进行分层控制的能力。deny 指令会限制对给定上下文的访问，allow 指令与 deny 功能
相反，它们的值可以是定值 IP 地址、IPv4 或 IPv6 地址、无类别域间路由(CIDR: Classless Inter-Domain Routing)、关键字或 UNIX 套接字。IP 限制的常用解决方案是，允许一个内部的 IP 地址访问资源，拒绝其它所有 IP 地址的访问来实现对资源的访问控制。

### 2.11.2 跨域资源共享控制

- 问题:

项目资源部署在其它域名，允许跨域的访问请求使用这些资源。

- 解决方案：

通过对不同请求方法设置对应的 HTTP 消息头实现跨域资源共享：

```nginx
map $request_method $cors_method {
    OPTIONS 11;
    GET 1;
    POST 1;
    default 0;
}

server {
    ...

    location / {
        if \($cors\_method ~ '1'\) {
            add\_header 'Access-Control-Allow-Methods' 'GET,POST,OPTIONS';
            add\_header 'Access-Control-Allow-Origin' '\*.example.com';
            add\_header 'Access-Control-Allow-Headers'
                        'DNT,
                        Keep-Alive,
                        User-Agent,
                        X-Requested-With,
                        If-Modified-Since,
                        Cache-Control,
                        Content-Type';
        }



        if \($cors\_method = '11'\) {
            add\_header 'Access-Control-Max-Age' 1728000;
            add\_header 'Content-Type' 'text/plain; charset=UTF-8';
            add\_header 'Content-Length' 0;
            return 204;
        }
    }
}
```

- 结论：

这个示例包含很多内容，首先使用 map 指令将 GET 和 POST 请求分入同一组。OPTIONS请求方法向客户端返回有关此服务器的CORS规则的称为预先请求的信息。在配置中 GET、POST、OPTIONS 请求都允许跨域访问资源。Access-Controll-Allow-Origin 消息头设置允许请求服务器资源的域名，当客户端域名匹配该设置的域名规则时，则可以访问服务器资源。预检请求可以缓存 客户端为1,728,000秒，或20天

## 2.12 访问限制

限制控制的合理使用对于服务器来讲能够有效阻止攻击者攻击请求。NGINX 服务器内置多种限制控制模块。本章将深入讲解访问连接数、请求速率和带宽限制等功能。首先需要区分什么是连接(connections) 和 请求(requests):连接(TCP 连接)是位于传输层的协议，一个 HTTP 请求会产生一个连接，所以它们是不同的东西。浏览器与服务器之间的交互允许打开多个连接，这样可以同时发起多个请求。然而， HTTP/1 和 HTTP/1.1 协议，同一时间仅能处理一个连接，直到 HTTP/2 才突破次限制，支持同时处理多个连接。本章将学习相关限制特性，实现对服务的合理使用。

### 2.12.1 连接数限制

- 问题:

基于给定的规则如 IP 地址，实现请求连接数。

- 解决方案：

使用 `limit_conn_zone` 指令构建存储当前连接数的内存区域；然后，使用 `limit_conn` 指令设置支持的连接数：

```nginx
http {
    limit\_conn\_zone $binary\_remote\_addr zone=limitbyaddr:10m;
    limit\_conn\_status 429;
    ...
    server {
        ...
        limit\_conn limitbyaddr 40;
        ...
    }
}
```

配置中创建了一个名为 limitbyaddr 的存储容量为 10 M 的共享内存，键名则为客户端二进制的 IP 地址。limit_conn 指令接收两个参数：一个是 limit_conn_zone 创建的名称 limitbyaddr，和支持的连接数 40 。limit_conn_status 指令定义了当连接数超过 40 个时的响应状态码。limit_conn 和 limit_conn_status 指令能够在 HTTP、server 和 location 上下文中使用。

- 结论：

合理使用连接数限制，可以是服务器的资源被各个客户端合理使用。使用的关键在于定义一个合理的存储键名。本例中基于 IP 地址作为存储键名不是一个好的选择，因为，一旦有许多用户通过同一网络访问服务，便会限制该 IP地址的所有用户的访问连接数，这很不合理。limit_conn_zone 仅在 http 上下文中可用可以使用所有的 NGINX 变量来构建限制键名。通过使用能够识别用户会话的变量如 cookie，有利于合理使用连接控制功能。limit_conn_status 默认状态码是 503 服务不可用。例子中使用 429 因为服务是可用的，而 500 级的响应码表示服务器内部错误，而 400 级的响应码表示客户端错误。

### 2.12.2 限制上传下载速度

- 问题:

依据某些规则对用户请求进行限速，如通过用户 IP 地址进行限速。

- 解决方案：

利用 rate-limiting 模块实现对请求限速：

```nginx
http {
    limit\_req\_zone $binary\_remote\_addr zone=limitbyaddr:10m rate=1r/s;
    limit\_req\_status 429;
    ...
    server {
        ...
        limit\_req zone=limitbyaddr burst=10 nodelay;
        ...
    }
}
```

实例中，创建了一个 10 M 存储空间的名为 limitbyaddr 的共享内存，并使用二进制的客户端 IP 地址作为键名。limit_req_zone 还设置了访问速度。limit_req 指令主要包含两个可选参数：zone 和 burst。zone 参数值即为 limit_req_zone 指令中 zone 参数定义的存储空间名。当用户请求超出限速设置时，超出的请求将会存储至 burst 定义的缓冲区，直至也超出请求限速缓冲速率，这是将响应 429 状态码给客户端。burst 参数默认值为 0。此外，limit_req 还有第三个参数 nodelay：它的功能是提供瞬时处理 rate + burst 个请求的能力。limit_req_status 参数用于设置超出速率请求响应给客户端的状态码，默认是 503，示例中设置为 429。limit_req_status 和 limit_req 指令适用于 HTTP、server 和 location 上下文。limit_req_zone 指令仅能在 HTTP 上下文中使用。

- 结论：

rate-limiting 模块在项目中非常有用，通过防止瞬间爆发的请求，为每个用户提供高质量的服务。使用限速模块有诸多理由，其一是处于安全方面考虑。如在登录页面设置严格的限速控制，拒绝暴力攻击。如果没有依据用户实现限速功能，可能会导致其他用户无法使用服务或浪费了服务器资源。rate-limiting 模块有点类似上一章节中讲解的限制连接模块。限速设置可以依据每秒限速，也可依据每分钟进行限速。当用户请求满足限速条件时，请求将被记入日志中。另外，还有一条指令没有在示例中给出：limit_req_log_level 指令设置限速日志级别，它默认值为 error 级别，您还可以设置为 info、notice 或 warn 级别。

### 2.12.3 限制带宽

- 问题:

需要依据客户端，限制它们下载速度。

- 解决方案：

使用 NGINX 服务器的 limit_rate 和 limit_rate_after 指令实现客户端响应速度：

```nginx
location /download/ {
    limit\_rate\_after 10m;
    limit\_rate 1m;
}
```

location 块级指令设置了对于匹配 /download/ 前缀的 URI 请求，当客户端下载数据达到 10 M以后，对其下载速度限制在 1 M 以内。不过该带宽限制功能仅仅是针对单个连接而言，因而，可能实际使用中需要配合使用连接限制和带宽限制实现下载限速。

- 结论：

limit_rate_after 和 limit_rate 使 NGINX 能够以您指定的方式在所有客户端上共享其上传带宽。limit_rate 和 limit_rate_after 指令可在几乎所有的上下文中使用，如 http、server、location、location 指令内的 if 指令，不过 limit_rate 指令还可以通过 $limit_rate 变量来设置带宽。limit_rate_after 指令表示在客户端使用多少流量后，将启用带宽限制功能。limit_rate 指令默认限速单位为字节(byte)，还可以设置为 m (兆字节) 和 g (吉字节)。这两条指令的默认值都是 0，表示不对带宽进行任何限制。另外，该模块提供以编码方式对客户端带宽进行限速。

## 2.23 数据加密

虽然总体上互联网环境危机四伏，但并非没有解决方法。随着 Let's 加密和 Amazon Web 服务的出现，在传输中传输对信息加密变得更加容易，也更容易实现。这两个服务都提供免费的证书可供开发这使用。这些免费证书，使用户敏感信息保护不再成为技术障碍。然并非所有的证书在保护敏感信息的能力都是相同的，不过启用总比不用强。本章将学习客户端与 NGINX 数据加密和 NGINX 服务器与代理服务(upstream services)的数据加密解决方案。

### 2.13.1 客户端加密

- 问题:

客户端与 NGINX 服务器之间的请求数据需要加密处理。

- 解决方案：

启用 ngx_http_ssl_module 或 ngx_stream_ssl_module 其中之一的 NGINX SSL 模块对数据进行加密：

```nginx
http {
    \# All directives used below are also valid in stream
    server {
        listen 8433 ssl;
        ssl\_protocols TLSv1.2;
        ssl\_ciphers HIGH:!aNULL:!MD5;
        ssl\_certificate /usr/local/nginx/conf/cert.pem;
        ssl\_certificate\_key /usr/local/nginx/conf/cert.key;
        ssl\_session\_cache shared:SSL:10m;
        ssl\_session\_timeout 10m;
    }
}
```

实例在 server 块级指令中设置监听启用 ssl 加密的 8843 端口。使用的 ssl 协议为 TLS1.2 版本。服务器有访问 SSL 证书及密钥目录的权限。另外，服务器和客户端交互采用最高强度加密数据。ssl_sesson_cache 和 ssl_session_timeout 指令用于设置会话存储内存空间和时间，除这两个指令外，还有一些与会员有关的指令，可以用于提升性能和安全性。但是，指定一个没有默认值的将转向关闭默认的内置会话缓存。

- 结论：

安全传输层是加密传输数据的常用手段。在写作本书时，传输层安全协议(TSL)是安全套接字层协议(SSL)的默认协议，因为，现在认为 1.0 到 3.0 版本的 SSL 协议都是不安全的。尽管安全协议的名称有所不同，但无论 TSL 协议还是 SSL 协议它们的最终目的都是构建一个安全的套接层。NGINX 服务器让你能在服务与客户端之间构建加密的数据传输，保证业务与用户数据安全。使用签名证书时，需要将证书与证书颁发机构链连接起来。证书和颁发机构通信时时，你的证书应该在文件链中。如果您的证书颁发机构在链中提供了许多文件，它也能够提供它们分层的顺序。SSL 会话缓存性能通过不带版本信息和数据加密方式的 SSL / TLS 协议实现。

### 2.13.2 Upstream 模块加密

- 问题:

需要在 NGINX 与 upstream 代理服务器之间依据具体规则构建安全通信。

- 解决方案：

使用 http 模块的 ssl 指令构建具体的 SSL 通信规则:

```nginx
location / {
    proxy\_pass https://upstream.example.com;
    proxy\_ssl\_verify on;
    proxy\_ssl\_verify\_depth 2;
    proxy\_ssl\_protocols TLSv1.2;
}
```

示例中配置了 NGINX 与代理服务器之间通信的 SSL 规则。首先启用安全传输校验功能，并将 NGINX 与代理服务器之间的证书校验深度设置为 2 层。proxy_ssl_protocols 指令用于设置使用 TSL 1.2 版本协议，它的默认值是不会校验证书，并可以使用所有版本 TLS 协议。

- 结论：

HTTP proxy 模块的指令繁多，如果需要启用安全传输功能，至少也需要开启校验功能。此外，我们还可以对 proxy_pass 指令设置协议，来实现 HTTPS 传输。不过，这种方式不会对被代理服务器的证书进行校验。其它的指令，如 proxy_ssl_certificate 和proxy_ssl_certificate_key 指令，用于配置被代理服务器待校验证书目录。另外，还有 proxy_ssl_crl 和 无效证书列表功能，用于列出无需认证的证书。这些 proxy 模块的 SSL 指令能够助你构建安全的内部服务通信和互联网通信。

## 2.20 实战加密技巧

### 2.20.1 HTTPS 重定向

我们的系统通常是分层的，所以安全策略需要依据不同的分层架构指定解决方案。在本书的第二部分，已经介绍了诸多安全策略方案。其中的部分章节中的解决方案能够用于加强安全防御能力。在这个章节，将从实战角度出发，讲解构建安全的 HTTPS 协议和 NGINX 服务器的方法。

- 问题:

需要将用户请求从 HTTP 协议重定向至 HTTPS 协议。

- 解决方案：

通过使用 rewrite 重写将所有 HTTP 请求重定向至 HTTPS:

```nginx
server {
    listen 80 default\_server;
    listen \[::\]:80 default\_server;
    server\_name \_;
    return 301 https://$host$request\_uri;
}
```

server 块级指令配置了用于监听所有 IPv4 和 IPv6 地址的 80 端口，return 指令将请求及请求 URI 重定向至相同域名的 HTTPS 服务器并响应 301 状态码给客户端。

- 结论：

在必要的场景下将 HTTP 请求重定向至 HTTPS 请求对系统安全来说很重要。有时，我们并不需要将将所有的用户请求都重定向至 HTTPS 服务器，而仅需将包含用户敏感数据的请求重定向至 HTTPS 服务即可，比如用户登录服务。

## 2.20.3 启用 HTTP 严格传输加密功能

- 问题:

需要告知浏览器不要使用 HTTP 发送请求

- 解决方案：

通过设置 Strict-Transport-Security 响应头不信息，启用 HTTP Strict Transport Security 策略，告知浏览器不支持 HTTP 请求:

```nginx
add_header Strict-Transport-Security max-age=31536000;
```

这里，我们将 Strict-Transport-Security 消息头有效期设置为 1 年，其作用是，当用户发起一个 HTTP 请求时，浏览器在内部做一个重定向，将所有请求直接通过 HTTPS 协议访问。

- 结论：

这是因为即使我们在服务器内部启用了 HTTPS 重定向功能，但浏览器端依然是 HTTP 请求，这可能会被中间人攻击，导致用户敏感数据泄露。这时候 HTTPS 重定向功能无法保证数据的安全性。当使用 Strict-Transport-Security 头时，浏览器将不会发送未被加密的 HTTP 请求，取而代之的是 HTTPS 请求，有效杜绝不安全的请求访问。

# 三、部署和运维

## 3.29 访问日志、错误日志和请求调用栈的调试和问题跟踪

对 NGINX 服务器进行调优会让你成为使用 NGINX 服务器的艺术家。对服务器或应用进行性能调优受影响因素颇多，包括但不限于：具体环境、用例、项目依赖和物理设备等。对项目在测试期间进行性能瓶颈测试调优十分常见，测试的目的是将服务测试直至遇到性能瓶颈、确定性能瓶颈、调优、在重复测试直至达到预期性能为止。本章，我们将学习自动化测试工具及测试结果进行优化处理；还将学习对连接的调优，以保持客户端与服务器的连接，和通过调优使服务器提供更强的连接能力。

### 3.29.1 配置访问日志

- 问题:

需要配置自定义格式的访问日志(access log)

- 解决方案：

配置访问日志格式：

```nginx
http {
    log_format geoproxy
    '[$time_local] $remote_addr '
    '$realip_remote_addr $remote_user '
    '$request_method $server_protocol '
    '$scheme $server_name $uri $status '
    '$request_time $body_bytes_sent '
    '$geoip_city_country_code3 $geoip_region '
    '"$geoip_city" $http_x_forwarded_for '
    '$upstream_status $upstream_response_time '
    '"$http_referer" "$http_user_agent"';
    ...
}
```

这个日志配置被命名为 `geoproxy`，它使用许多 NGINX 变量来演示 NGINX 日志记录功能。接下来详细讲解配置选项中各个变量的具体含义：

当用户发起请求时，会记录服务器时间( $time_local )、用于 NGINX 处理 geoip_proxy 和 realip_header 指令的打开连接的 IP 地址和客户端 IP 地址；$remote_user 值为通过基本授权的用户名称；之后记录 HTTP 请求方法( $request_method )、协议( $server_protocol )和 HTTP 方法( $scheme：http 或 https ) ；当然还有服务器名称( $server_name )、请求的 URI 和响应状态码。除基本信息外，还有一些统计的结果数据：包括请求处理的毫秒级时间($request_time)、服务器响应的数据块大小( $body_bytes_sent )。此外，客户端所在国家($geoip_city_country_code3 )、地区( $geoip_region )和城市信息( $geoip_city )也被记录在内。变量 $http_x_forwarded_for用于记录由其它代理服务器发起的请求的 X-Forwarded-For 头消息。upstream 模块中一些数据也被记录到日志里：被代理服务器的响应状态码( $upstream_status )和服务器处理时间( $upstream_response_time )。请求来源( $http_referer )和用户代理( $http_user_agent ) 也有被记录在日志里。从上面可以看出 NGINX 日志记录功能还是非常强大和灵活的，不过用于定义日志格式的 log_format 指令仅适用于 http 块级指令内，这一点需要注意。

此日志配置呈现的日志条目如下所示：

```nginx
[25/Nov/2016:16:20:42 +0000] 10.0.1.16 192.168.0.122 Derek
GET HTTP/1.1 http www.example.com / 200 0.001 370 USA MI
"Ann Arbor" - 200 0.001 "-" "curl/7.47.0"
```

如果需要使用这个日志配置，需要结合使用 access_log 指令，access_log 指令接收一个日志目录和使用的配置名作为参数：

```nginx
server {
    access_log /var/log/nginx/access.log geoproxy;
    ...
}
```

access_log 能在多个上下文使用，每个上下文中可以定义各自的日志目录和日志记录格式。

- 结论：

NGINX 中的日志模块允许您为不同的场景配置日志格式，以便查看不同的日志文件。在实际运用中，为不同上下文配置不同的日志会非常有用，记录的日志内容可以简单的信息，也可以事无巨细的记录所有必要信息。不仅如此，日志内容除了支持文本也能记录 JSON 格式和 XML 格式数据。实际上 NGINX 日志有助于您了解服务器流量、客户端使用情况和客户端来源等信息。此外，访问日志还可以帮助您定位与上游服务器或特定 uri 相关的响应和问题；对于测试来讲，访问日志同样有用，它可以用于分析流量情况，模拟真实的用户交互场景。日志在故障排除、调试、应用分析及业务调整中作用是不可或缺的。

### 3.29.2 配置错误日志

- 问题:

需要更深入的定位 NGINX 服务器问题，以配置错误日志。

- 解决方案：

使用 error_log 指令定义错误日志目录及记录错误日志的等级:

```nginx
error_log /var/log/nginx/error.log warn;
```

error_log 指令配置时需要一个必选的日志目录和一个可选的错误等级选项。除 if 指令外，error_log 指令能在所有的上下文中使用。错误日志等级包括：`debug、info、notice、warn、error、crit、alert 和 emerg`。给出的日志等级顺序就是记录最小到最严谨的日志等级顺序。需要注意的是 debug 日志需要在编译 NGINX 服务器时，带上 --with-debug 标识才能使用。

- 结论：

请牢记当服务器配置出错时，首先需要查看错误日志以定位问题。当然，错误日志也是定位应用服务器(如 FastCGI 服务)的利器。通过错误日志，我们可以调试 worder 进程连接错误、内存分配、客户端 IP 和 应用服务器等问题。错误日志格式虽然不支持自定义日志格式；但是，它同样记录当前时间、日志等级和具体信息等数据。

### 3.29.3 将日志记录到 syslog

- 问题:

需要将错误日志通过 syslog 服务记录到集中日志服务器。

- 解决方案：

在使用 error_log 和 access_log 指令时，将日志发送至 syslog 监听器:

```nginx
error_log syslog:server=10.0.1.42 debug;
access_log syslog:server=10.0.1.42,tag=nginx,severity=info geoproxy;
```

error_log 和 access_log 指令的 syslog 参数紧跟冒号(:)和一些参数选项。包括：必选的 server 标记表示需要连接的 IP、DNS 名称或 UNIX 套接字；可选参数有 facility、severity、tag 和 nohostname。server 参数接收带端口的 IP 地址或 DNS 名称；默认是 UDP 514 端口。facility 参数设置 syslog 的类型(facility)，值是 syslog RFC 标准定义的 23 个值中的一个(@todo)。tag 参数表示日志文件中显示时候的标题，默认值是 nginx。severity 设置消息严重程度，默认是 info 级别日志。nohostname 选项，禁止将 hostname 域添加到syslog的消息头中。

- 结论：

syslog 是用于在单台服务器或服务器集群中记录和收集日志的标准协议。在多个主机上运行相同服务的多个实例时，将日志发送到集中位置有助于调试，这称为聚合日志。聚合日志允许您在一个地方查看日志，而不必切换不同服务器，并通过时间戳将日志文件集成在一起。常见聚合日志解决方案有ElasticSearch、Logstash、Kibana 和 ELK Stack。但 NGINX 通过发送日志到 syslog 监听器，能够很容易的将 access_log 和 error_log 指令捕捉的日志发送到聚合日志服务器上。

### 3.29.3 请求调用栈

- 问题:

需要结合 NGINX 日志和应用日志，查看请求调用栈。

- 解决方案：

使用 request 标识，并将标识写入到应用日志里：

```nginx
log_format trace '$remote_addr - $remote_user [$time_local] '
                '"$request" $status $body_bytes_sent '
                '"$http_referer" "$http_user_agent" '
                '"$http_x_forwarded_for" $request_id';
upstream backend {
    server 10.0.0.42;
}
server {
    listen 80;

    add\_header X-Request-ID $request\_id; \# Return to client

    location / {
        proxy_pass http://backend;
        proxy_set_header X-Request-ID $request_id; \#Pass to app
        access_log /var/log/nginx/access_trace.log trace;
    }
}
```

示例中，配置了名为 trace 的访问日志格式，并在日志中使用 $request_id 参数。同时，通过 proxy_set_header 指令将 request 标记(request ID)设置到请求头里，当请求匹配到 location / 前缀，请求被转发到 upstream 模块，这样同一个 request 标识就能记录到应用服务器日志里；此外，通过 add_header 指令将 reqeust 标识设置到响应消息头，供客户端使用。

- 结论：

该功能在 NGINX Plus R10 版本和 NGINX 开源版的 1.11.0 版本可用，$request_id 提供了一个随机生成的 32 个十六进制字符的字符串，这些字符可以用来唯一地标识请求。通过将此标识符传递给客户端和应用服务器，可以将日志与请求关联起来。客户端会收到唯一的 request 标识，服务端也能使用该标识进行日志筛选。应用服务器使用时，需要获取这个消息头，以建立日之间的关联。基于这个特性，NGINX 能够构建从客户端请求到应用服务器做出响应的整个请求调用周期的所有日志信息之间的关联。

## 3.30 性能调优

对 NGINX 服务器进行调优会让你成为使用 NGINX 服务器的艺术家。对服务器或应用进行性能调优受影响因素颇多，包括但不限于：具体环境、用例、项目依赖和物理设备等。对项目在测试期间进行性能瓶颈测试调优十分常见，测试的目的是将服务测试直至遇到性能瓶颈、确定性能瓶颈、调优、在重复测试直至达到预期性能为止。本章，我们将学习自动化测试工具及测试结果进行优化处理；还将学习对连接的调优，以保持客户端与服务器的连接，和通过调优使服务器提供更强的连接能力。

### 3.30.1 使用负载测试工具实现自动化测试

- 问题:

使用负载测试工具实现自动化测试

- 解决方案：

使用 HTTP 负载测试工具：如 Apache JMeter/ Locust/ Gatling/或团队自研的负载工具。为测试定制测试配置，并对服务器进行全面测试，基于测试结果量化性能指标；之后，逐步增加用户数增加并发量，以模拟生产环境真实请求，找出性能瓶颈优化；如此反复，直至达到项目的预期性能。

- 结论：

使用自动化的测试工具来定义您的测试，可以让您通过一个一致的测试来找出对 NGINX 进行调优的基准。性能测试必须是可重复的，通过对性能测试结果进行科学分析。在对 NGINX 配置进行优化前，需对服务器进行测试确定标准，这样，才能确定之后的配置优化是否实现了性能的优化。对每个配置优化进行度量，将帮助您确定性能得以提升的根源。

### 3.30.2 启用客户端长连接

- 问题:

增加单个连接的请求数，同时增加空闲连接(idle connections)的的连接时长。

- 解决方案：

keepalive_requests 和 keepalive_timeout 指令允许变更单个连接的最大请求数和空闲连接的连接时长：

```nginx
http {
    keepalive_requests 320;
    keepalive_timeout 300s;
    ...
}
```

keepalive_requests 默认为 100，keepalive_timeout 的默认值为 75 秒。

- 结论：

一般情况下，keepalive_requests 和 keepalive_timeout 的默认配置，能够满足客户端的请求，因为，现代浏览器能为不同域名打开多个连接。但对于同一个域名仅能同时发起 10 以内的请求，这将带来性能瓶颈。CDN 的实现原理是启用多个域名指向内容服务器，并以编码的方式指定使用的域名，以使浏览器能够打开更多的连接。你会发现使用更多的请求连接数和连接时长配置，在客户端需要频繁更新数据能提升服务器性能。

### 3.30.3 启用 upstream 模块长连接

- 问题:

需要增加代理服务器与被代理服务器的连接数，提升服务器性能。

- 解决方案：

在 upstream 会计指令中使用 keepalive 指令保持代理服务与被代理服务器连接以复用：

```nginx
proxy_http_version 1.1;
proxy_set_header Connection "";
upstream backend {
    server 10.0.0.42;
    server 10.0.2.56;
    keepalive 32;
}
```

keepalive 指令会为每个 NGINX worker 进程创建一个连接缓存，表示每个 worker 进程能保持打开的空闲连接的最大连接数量。如果要使 keepalive 指令正常工作，在 upstream 指令上使用的 proxy 模块指令则是必须的。proxy_http_version 指令表示启用的 http 1.1 版本，它允许在单个连接上发送多个请求；proxy_set_header 指令删除 connection 消息头的默认值close，这样就允许保持连接的打开状态。

- 结论：

当需要保持代理服务器与被代理服务器的连接打开状态，以节省启动连接所需的时间；同时，需要将 worker 进程收到的请求分发值空闲的连接直接处理。有一点需要注意，开启的连接数可以多于 keepalive 配置的连接数，因为开启的连接数和空闲连接数不是同一个东西。keepalive 配置的连接数应尽量少，以确保新的请求能够被分发到被代理服务器。这条配置技巧能够通过减少请求连接的生命周期的手段，提升服务器性能。

### 3.30.4 启用响应缓冲区

- 问题:

将服务器对客户端的响应写入内存缓冲区而不是文件里。

- 解决方案：

调整代理模块的缓存区设置，允许 NGINX 服务器将响应消息体写入内存缓冲区：

```nginx
server {
    proxy_buffering on;
    proxy_buffer_size 8k;
    proxy_buffers 8 32k;
    proxy_busy_buffer_size 64k;
    ...
}
```

proxy_buffering 值可以使 on 或 off，默认是 on。proxy_buffer_size 指令表示用于读取来自代理服务器响应的缓冲大小，依据平台不同它的默认值为 4k 或 8k。proxy_buffers 指令包含两个值，支持的缓存区个数和单个缓存区容量大小，默认是 8 个缓存区，依据平台不同单个缓存区默认容量为 4k 或 8k。proxy_busy_buffer_size 指令用于配置未完全读取响应时直接响应客户端的缓冲区大小，它的空间一般为 proxy_buffers 的两倍为最佳。

- 结论：

代理缓存能显著提升代理服务性能，这取决于响应内容的大小。开启缓冲区设置应当仔细测试响应内容的平均大小，并进行大量测试和调试，否则可能引发副作用。而如果将缓存区大小设置的非常大也不行，这回占用大量的 NGINX 内存。一种方案是将缓冲区大小设置为与最大响应消息相同以提升性能。

### 3.30.5 启用访问日志缓冲区

- 问题:

当系统处于负载状态时，启用日志缓冲区以降低 NGINX worker 进程阻塞。

- 解决方案：

设置 access_log 的 buffer 和 flush 参数：

```nginx
http {
    access_log /var/log/nginx/access.log main buffer=32k flush=1m;
}
```

buffer 参数用于设置，写入文件前的缓冲区内存大小；flush 参数设置缓冲区内日志在缓冲区内存中保存的最长时间。

- 结论：

将日志数据缓冲到内存中可能是很小的一个优化手段。但是，对于有大量请求的站点和应用程序的磁盘读写和 CPU 使用性能有重大意义。buffer 参数的功能是当缓冲区已经写满时，日志会被写入文件中；flush 参数的功能是，当缓存中的日志超过最大缓存时间，也会被写入到文件中，不过也有不足的地方即写入到日志文件的日志有些许延迟。
