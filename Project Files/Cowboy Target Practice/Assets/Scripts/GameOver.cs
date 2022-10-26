using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;

public class GameOver : MonoBehaviour
{
    public IntData life;
    public UnityEvent LifeEvent;

    public void CheckLives()
    {
        if (life.value == 0) ;
        {
            LifeEvent.Invoke();
        }
    }
}
