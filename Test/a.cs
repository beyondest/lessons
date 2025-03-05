using System;
using UnityEngine;
using UnityEngine.EventSystems;

public class RTSCameraController : MonoBehaviour
{
    public static RTSCameraController instance;
    Vector3 newPosition;
    Vector3 dragStartPosition;
    Vector3 dragCurrentPosition;
    float movementSpeed;


    [SerializeField] Transform cameraTransform;
    public Transform followTransform;

    [Header("Config")]
    [SerializeField] float normalSpeed = 0.01f;
    [SerializeField] float movementSensitivity = 1f;
    [SerializeField] float edgeSize = 50f;  // Affect the sensitivity of edge scrolling

    private void OnEnable()
    {

    }




    private void Start()
    {
        instance = this;
        newPosition = transform.position;
        movementSpeed = normalSpeed;
    }

    private void Update()
    {
        if (GameController.isPaused) return;
        if (Application.isFocused == false) return;

        if (followTransform != null)
        {
            transform.position = followTransform.position;
        }
        else
        {
            HandleEdgeScrollInput();
            transform.position = Vector3.Lerp(transform.position, newPosition, Time.deltaTime * movementSensitivity);
        }

    }

    private void OnMiddleClick( RaycastHit hit)
    {
        Plane plane = new Plane(Vector3.up, Vector3.zero);
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        float entry;
        if (plane.Raycast(ray, out entry))
        {
            dragStartPosition = ray.GetPoint(entry);
        }
    }

    private void OnMiddleClicking( RaycastHit hit)
    {
        Plane plane = new Plane(Vector3.up, Vector3.zero);
        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        float entry;
        if (plane.Raycast(ray, out entry))
        {
            dragCurrentPosition = ray.GetPoint(entry);
            newPosition = transform.position + dragStartPosition - dragCurrentPosition;
        }
    }
    private void OnMiddleClickUp( RaycastHit hit)
    {
        dragStartPosition = Vector3.zero;
        dragCurrentPosition = Vector3.zero;
        newPosition = transform.position;
    }

    private void HandleEdgeScrollInput()
    {
        if (Input.mousePosition.y >= Screen.height - edgeSize)
        {
            newPosition += (transform.forward * movementSpeed);
            CursorManager.instance.SetCursor(CursorManager.instance.cursorScrollUp);
        }
        else if (Input.mousePosition.y <= edgeSize)
        {
            newPosition += (transform.forward * -movementSpeed);
            CursorManager.instance.SetCursor(CursorManager.instance.cursorScrollDown);

        }
        else if (Input.mousePosition.x >= Screen.width - edgeSize)
        {
            newPosition += (transform.right * movementSpeed);
            CursorManager.instance.SetCursor(CursorManager.instance.cursorScrollDown);
        }
        else if (Input.mousePosition.x <= edgeSize)
        {
            newPosition += (transform.right * -movementSpeed);
            CursorManager.instance.SetCursor(CursorManager.instance.cursorScrollDown);
        }
        else
        {
            CursorManager.instance.SetCursor(CursorManager.instance.cursorScrollDefault);
        }
    }
}
