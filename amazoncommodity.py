import requests
r=requests.get("https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0?pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=W74J7H5GZ30RJRF23VG7&pf_rd_r=W74J7H5GZ30RJRF23VG7&pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e")
r.status_code
r.encoding=r.apparent_encoding
r.request.headers
kv={"User-Agent":"Mozilla/5.0"}
r=requests.get("https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0?pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=W74J7H5GZ30RJRF23VG7&pf_rd_r=W74J7H5GZ30RJRF23VG7&pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e",headers=kv)
r.status_code
r.encoding=r.apparent_encoding
r.text
r.request.headers
r.text
