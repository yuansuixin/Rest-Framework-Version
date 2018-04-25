

## 版本

- url中通过GET传参
  自定义的版本

- 使用内置的类


![Untitled-1-2018420213639](http://p693ase25.bkt.clouddn.com/Untitled-1-2018420213639.png)
- 这3个只需要在配置文件中设置就可以

- 在url路径中传参(推荐使用)

- 源码流程
    - 返回版本是在封装request之后，认证和权限之前做的

    - BaseVersioning对象


![Untitled-1-2018420213814](http://p693ase25.bkt.clouddn.com/Untitled-1-2018420213814.png)

- 里面有个rest framework封装的reverse（），内反向生成url，不需要指定版本，会自动生成，其实就是当前url的版本，本质上底层是使用了Django自带的reverse()实现的。

```
class UsersView(APIView):
    def get(self,request,*args,**kwargs):
        self.dispatch()
        # 获取版本
        print(request.version)
        # 获取版本的对象
        print(request.versioning_scheme)
        # 内置的反向生成url，不需要指定版本，会自动生成，其实是当前url的版本
        u1 = request.versioning_scheme.reverse(viewname='uuu',request=request)
        print(u1)
        # 使用Django内置的反向生成url,必须要指定版本
        u2 = reverse(viewname='uuu',kwargs={'version':1})
        print(u2)
        return HttpResponse('用户列表')
```
- 除了这些，版本的实现还有很多


  ![Untitled-1-2018420214715](http://p693ase25.bkt.clouddn.com/Untitled-1-2018420214715.png)

##### 总结

- 使用   配置文件
- 路由系统
- 视图
- 源码流程


[中文文档详细解析](https://yuansuixin.github.io/2018/02/21/rest-framework-version/ "详细解析")




