using System.Collections;
using UnityEngine;
using UnityEngine.Events;


public class OnClickBehavior : MonoBehaviour
{
    public UnityEvent onClickEvent, noClickEvent;

    public void OnMouseDown()
    {
        onClickEvent.Invoke();
    }
}

