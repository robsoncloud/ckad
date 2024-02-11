for i in {1..20}; do
   kubectl exec --namespace=kube-public curl -- sh -c 'test=`wget -qO- -T 2  http://webapp-01.liveness.svc.cluster.local/ready 2>&1` && echo "$test OK" || echo "Failed"';
   echo ""
done

# k run curl --image=byrnedo/alpine-curl:latest -n kube-public -- sleep 5000 
