using System.Collections;
using System.Collections.Generic;
using JetBrains.Annotations;
using UnityEngine;

public class DestroyOnClick : MonoBehaviour
{
    public void DestroyGameObject(Collider other)
    {
        Destroy(other.gameObject);
    }
}
