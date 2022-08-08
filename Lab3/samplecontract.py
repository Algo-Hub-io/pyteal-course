#samplecontract.py
# This file is from the Algorand documentation - https://developer.algorand.org/docs/get-details/dapps/pyteal/#final-product
from pyteal import *

## 1. Update App Name
"""Basic Counter Application"""

def approval_program():
    handle_creation = Seq([
        App.globalPut(Bytes("Count"), Int(0)),
        Return(Int(1))
    ])

    # 2. Change handle_optin to return 1
    handle_optin = Return(Int(0))
    handle_closeout = Return(Int(0))
    handle_updateapp = Return(Int(0))
    handle_deleteapp = Return(Int(0))
    scratchCount = ScratchVar(TealType.uint64)
    # 3 - add local scratch var

    # 4 - rename add and deduct to add_global and deduct_global
    add = Seq([
        scratchCount.store(App.globalGet(Bytes("Count"))),
        App.globalPut(Bytes("Count"), scratchCount.load() + Int(1)),
        Return(Int(1))
    ])

    deduct = Seq([
        scratchCount.store(App.globalGet(Bytes("Count"))),
         If(scratchCount.load() > Int(0),
             App.globalPut(Bytes("Count"), scratchCount.load() - Int(1)),
         ),
         Return(Int(1))
    ])

    # 5 - create a local version of add and deduct

    # 6 -Update the handle_noop conditions to use global and add local options
    handle_noop = Seq(
        Assert(Global.group_size() == Int(1)), 
        Cond(
            [Txn.application_args[0] == Bytes("Add"), add], 
            [Txn.application_args[0] == Bytes("Deduct"), deduct]
        )
    )


    program = Cond(
        [Txn.application_id() == Int(0), handle_creation],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop]
    )

    return compileTeal(program, Mode.Application, version=5)


def clear_state_program():
    program = Return(Int(1))
    return compileTeal(program, Mode.Application, version=5)

# 7 - update the file to 
# print out the results
print(approval_program())
print(clear_state_program())
