package com.example.pkucat.post.list;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProviders;
import androidx.recyclerview.widget.DividerItemDecoration;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.pkucat.R;
import com.example.pkucat.post.PostEntity;

import java.util.ArrayList;

public class PostFragment extends Fragment {

    private static final String ARG_SECTION_NUMBER = "section_number";
    private int index = 1;

    private View view;
    private ArrayList<PostEntity> postEntities;

    public static PostFragment newInstance(int index) {
        PostFragment fragment = new PostFragment();
        Bundle bundle = new Bundle();
        bundle.putInt(ARG_SECTION_NUMBER, index);
        fragment.setArguments(bundle);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        PostViewModel postViewModel = ViewModelProviders.of(this).get(PostViewModel.class);
        if (getArguments() != null) {
            index = getArguments().getInt(ARG_SECTION_NUMBER);
            // 这里是对不同tab下的界面处理
            System.out.println(index);
        }
        postViewModel.setIndex(index);
        // TODO: 下拉刷新，上拉加载
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
                             ViewGroup container, Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.fragment_post, container, false);
        /*
        final TextView textView = root.findViewById(R.id.section_label);
        postViewModel.getText().observe(getViewLifecycleOwner(), new Observer<String>() {
            @Override
            public void onChanged(@Nullable String s) {
                textView.setText(s);
            }
        });
        return root;
        */

        // TODO: 搜索功能
        initData();
        initRecyclerView();
        return view;
    }

    private void initData() {
        postEntities = new ArrayList<>();
        // TODO: 获取动态
        for (int i = 0; i < 5; i++) {
            PostEntity postEntity = new PostEntity("", "User"+i, "Time", "POST"+i*10, new ArrayList<Integer>());
            if (i == 0) {
                if (getArguments() != null && getArguments().getInt(ARG_SECTION_NUMBER) == 1) {
                    postEntity.addImagePath(R.drawable.catexp);
                    postEntity.addImagePath(R.drawable.catexp0);
                    postEntity.addImagePath(R.drawable.catexp1);
                    postEntity.addImagePath(R.drawable.catexp2);
                    postEntity.addImagePath(R.drawable.demo);
                }
            }
            postEntities.add(postEntity);
        }
    }

    private void initRecyclerView() {
        RecyclerView mRecyclerView = view.findViewById(R.id.recyclerview_post);
        RecyclerViewAdapter mRecyclerViewAdapter = new RecyclerViewAdapter(this.getActivity(), postEntities);
        mRecyclerView.setAdapter(mRecyclerViewAdapter);
        // layout: vertical, horizontal, ...
        mRecyclerView.setLayoutManager(new LinearLayoutManager(this.getActivity(), LinearLayoutManager.VERTICAL, false));
        // dividing line
        mRecyclerView.addItemDecoration(new DividerItemDecoration(this.getActivity(), DividerItemDecoration.VERTICAL));
        mRecyclerViewAdapter.setOnItemClickListener(new RecyclerViewAdapter.OnItemClickListener() {
            @Override
            public void OnItemClick(View view, PostEntity data) {
                Toast.makeText(getActivity(), "Here it is: "+data.getAvatarPath(), Toast.LENGTH_SHORT)
                        .show();
            }
        });

    }
}
