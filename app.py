from flask import Flask, render_template, request
import os.path as osp
import pandas as pd

app = Flask(__name__)


src_dir = osp.dirname(__file__)
df_table = pd.read_csv(
    osp.join(src_dir, "Clusters", "table.csv"), encoding="ISO-8859-1"
)

app.debug = True


@app.route("/", methods=["GET"])
def index():
    titles = list(df_table["title"])
    return render_template("index.html", titles=titles)


@app.route("/cluster", methods=["GET"])
def get_cluster():
    df_cluster = pd.read_csv(
        osp.join(
            src_dir,
            "Clusters",
            f"{df_table[df_table['title']==request.args.get('titles')].iloc[0]['cluster']}.csv",
        )
    )
    df_cluster = df_cluster[["username", "tweet"]].sample(n=20)
    result=df_cluster.set_index("username").to_dict()["tweet"]
    return render_template("cluster.html", result=result)


# if __name__ == "__main__":
app.run()
