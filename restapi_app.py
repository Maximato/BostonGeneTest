from typing import List

from fastapi import FastAPI
from fastapi import HTTPException
from pandas import read_csv, Series
from pandas.core.computation.ops import UndefinedVariableError


app = FastAPI(title="Signatures")

signatures = read_csv("signatures.tsv", sep="\t", index_col=0)


@app.get("/sign", response_description="Signatures", description="Get signatures of patient")
async def sign(patient: str) -> Series:
    try:
        signature = signatures.loc[patient]
    except KeyError:
        raise HTTPException(404, f"There is no signatures for patient {patient}")
    return signature


@app.get("/query", response_description="Patients", description="Get satisfying the query patients")
async def query(q: str) -> List[str]:
    try:
        patients = list(signatures.query(q).index)
    except SyntaxError:
        raise HTTPException(404, "Wrong query format")
    except UndefinedVariableError:
        raise HTTPException(404, "Undefined variable")
    return patients
