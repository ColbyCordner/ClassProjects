using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[CreateAssetMenu]
public class IntData : ScriptableObject
{
    //Basic Information
    public string name;
    public int age;
    public int height;
    public int weight;

    public void Print()
    {
        Debug.Log(name + ": " + "is roughly " + age + "years old");
    }
}
    
