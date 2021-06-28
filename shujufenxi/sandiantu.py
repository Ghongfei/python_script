from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.charts import EffectScatter
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType


#
# c = (
#     Scatter()
#     .add_xaxis(Faker.choose())
#     .add_yaxis(
#         "类别1",
#         [list(z) for z in zip(Faker.values(), Faker.choose())],
#         label_opts=opts.LabelOpts(
#             formatter=JsCode(
#                 "function(params){return params.value[1] +' : '+ params.value[2];}"
#             )
#         ),
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="多维度数据"),
#         tooltip_opts=opts.TooltipOpts(
#             formatter=JsCode(
#                 "function (params) {return params.name + ' : ' + params.value[2];}"
#             )
#         ),
#         visualmap_opts=opts.VisualMapOpts(
#             type_="color", max_=150, min_=20, dimension=1
#         ),
#     )
#     .render("多维数据散点图.html")
# )
# print([list(z) for z in zip(Faker.values(), Faker.choose())])




# c = (
#     Scatter()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("A", Faker.values())
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="标题"),
#         xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
#         yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
#     )
#     .render("分割线.html")
# )




# c = (
#     Scatter()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("1", Faker.values())
#     .add_yaxis("2", Faker.values())
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="标题"),
#         visualmap_opts=opts.VisualMapOpts(type_="size", max_=150, min_=20),
#     )
#     .render("凸出大小散点图.html")
# )



# c = (
#     EffectScatter()
#     .add_xaxis(Faker.choose())
#     .add_yaxis("", Faker.values())
#     .set_global_opts(title_opts=opts.TitleOpts(title="散点图"))
#     .render("动态散点图.html")
# )



c = (
    EffectScatter()
    .add_xaxis(Faker.choose())
    .add_yaxis("", Faker.values(), symbol=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="标题"))
    .render("箭头动态散点图.html")
)