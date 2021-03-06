def consumer():
    r = ''
    while True:
        # yield不但可以返回一个值，它还可以接收调用者发出的参数。
        n = yield r
        if not n:
            return
        print('[CONSUMER]Consumer %s...' % n)
        r = '200 OK'

# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# 生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
def product(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCT]Product %s...' % n)
        r = c.send(n)
        print('[PRODUCT]Consumer return %s' % r)
    c.close()


# 注意到consumer函数是一个generator，把一个consumer传入produce后：
# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
if __name__ == '__main__':
    c = consumer()
    product(c)
