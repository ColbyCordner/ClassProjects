using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HumanInfo : MonoBehaviour
{
    public IntData Human;

    void start()
    {
        Debug.Log(Human.name);
    }
}
