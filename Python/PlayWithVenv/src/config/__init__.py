import pathlib
import tomllib

path = pathlib.Path(__file__).parent / "PlayWithVEnv.toml"
with path.open(mode="rb") as fp:
    appconfig = tomllib.load(fp)