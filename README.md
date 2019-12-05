### 生成样例

specs_info (规格信息) 

| 序号 | 字段名称               | 数据类型    | 是否为空 | 字段说明             |
| :--: | ---------------------- | ----------- | -------- | -------------------- |
|  1   | id                     | bigint(20)  | NO       | 规格编号             |
|  2   | product_id             | bigint(20)  | YES      | 商品编号             |
|  3   | specs_code             | varchar(32) | YES      | 规格编码             |
|  4   | specs_unit             | varchar(16) | YES      | 规格单位             |
|  5   | product_attr_value_ids | json        | YES      | 属性值id列表         |
|  6   | product_attr_map       | json        | YES      | 规格详情             |
|  7   | create_time            | timestamp   | YES      | 创建时间             |
|  8   | update_time            | timestamp   | YES      | 更新时间             |
|  9   | del_flag               | bit(1)      | YES      | 删除标识:0正常,1删除 |
