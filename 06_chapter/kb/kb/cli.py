import gevent
from gevent import monkey
monkey.patch_all()
import time
import click
import requests
from numpy import mean
from tqdm import tqdm


class Statistical:
    """统计类"""
    pass_number = 0
    fail_number = 0
    run_time_list = []


def running(url, request):
    """运行请求调用"""
    for _ in tqdm(range(request)):
        start_time = time.time()
        r = requests.get(url)
        if r.status_code == 200:
            Statistical.pass_number = Statistical.pass_number + 1
        else:
            Statistical.fail_number = Statistical.fail_number + 1

        end_time = time.time()
        run_time = round(end_time - start_time, 4)
        Statistical.run_time_list.append(run_time)


@click.command()
@click.argument('url')
@click.option('-u', '--user', default=1, help='运行用户的数量，默认 1', type=int)
@click.option('-q', '--request', default=1, help='单个用户请求数，默认 1', type=int)
def main(url, user, request):
    print(f"请求URL: {url}")
    print(f"用户数：{user}，循环次数: {request}")
    print("============== Running ===================")

    jobs = [gevent.spawn(running, url, request) for _url in range(user)]
    gevent.wait(jobs)

    print("\n============== Results ===================")
    print(f"最大:       {str(max(Statistical.run_time_list))} s")
    print(f"最小:       {str(min(Statistical.run_time_list))} s")
    print(f"平均:       {str(round(mean(Statistical.run_time_list), 4))} s")
    print(f"请求成功: {Statistical.pass_number}")
    print(f"请求失败: {Statistical.fail_number}")
    print("================== end ====================")


if __name__ == "__main__":
    main()
