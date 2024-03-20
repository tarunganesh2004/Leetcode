import java.util.Scanner;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}


public class mergeBetween {
    public static ListNode createLinkedList(Scanner scanner) {
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        System.out.print("Enter the elements: ");
        ListNode dummy = new ListNode();
        ListNode current = dummy;
        for (int i = 0; i < n; i++) {
            int value = scanner.nextInt();
            current.next = new ListNode(value);
            current = current.next;
        }
        return dummy.next;
    }

    public static void printLinkedList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        System.out.println();
    }
    
    public static ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode start = list1, end = list1;
        int index = 1;

        while (index <= b) {
            if (index == a) {
                start = end;
            }
            end = end.next;
            index++;
        }

        start.next = list2;
        while (list2.next != null) {
            list2 = list2.next;
        }
        list2.next = end.next;
        return list1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Create list1:");
        ListNode list1 = createLinkedList(scanner);
        System.out.println("List1 created: ");
        printLinkedList(list1);

        System.out.println("Create list2:");
        ListNode list2 = createLinkedList(scanner);
        System.out.println("List2 created: ");
        printLinkedList(list2);

        System.out.print("Enter the value of 'a': ");
        int a = scanner.nextInt();
        System.out.print("Enter the value of 'b': ");
        int b = scanner.nextInt();

        
        ListNode mergedList = mergeInBetween(list1, a, b, list2);

        System.out.println("Merged List:");
        printLinkedList(mergedList);

        scanner.close();
    }
}
